from pathlib import Path
import importlib.util
import sys

spec = importlib.util.find_spec("pytgcalls")
if not spec or not spec.submodule_search_locations:
    raise SystemExit("pytgcalls package not found; cannot apply compatibility fix")

package_dir = Path(next(iter(spec.submodule_search_locations)))
target = package_dir / "mtproto" / "pyrogram_client.py"
if not target.is_file():
    raise SystemExit(f"Expected PyTgCalls handler not found: {target}")

source = target.read_text(encoding="utf-8")
old = "chat_id = self.chat_id(data2[update.chat_id])"
new = """if getattr(update, "chat_id", None) is not None:
                chat = data2.get(update.chat_id) if isinstance(data2, dict) else None
                if chat is not None:
                    chat_id = self.chat_id(chat)
                elif getattr(update, "peer", None) is not None:
                    chat_id = self.chat_id(update.peer)
                else:
                    return
            elif getattr(update, "peer", None) is not None:
                chat_id = self.chat_id(update.peer)
            else:
                # Some Telegram update variants do not expose chat_id or peer.
                # Ignore the unrelated update instead of crashing Pyrogram's worker.
                return"""
if new in source:
    print("PyTgCalls UpdateGroupCall compatibility fix already applied")
elif old in source:
    target.write_text(source.replace(old, new, 1), encoding="utf-8")
    print("Applied PyTgCalls UpdateGroupCall compatibility fix")
else:
    raise SystemExit("Unrecognized PyTgCalls handler source; refusing unsafe patch")
