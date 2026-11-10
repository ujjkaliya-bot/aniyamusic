from pathlib import Path
import importlib.util

spec = importlib.util.find_spec("pytgcalls")
if not spec or not spec.submodule_search_locations:
    raise SystemExit("PyTgCalls package not found")

target = Path(next(iter(spec.submodule_search_locations))) / "mtproto" / "pyrogram_client.py"
if not target.is_file():
    raise SystemExit(f"PyTgCalls handler not found: {target}")

source = target.read_text(encoding="utf-8")
old = "chat_id = self.chat_id(data2[update.chat_id])"
new = """if getattr(update, "chat_id", None) is not None and update.chat_id in data2:
                    chat_id = self.chat_id(data2[update.chat_id])
                elif getattr(update, "peer", None) is not None:
                    chat_id = self.chat_id(update.peer)
                else:
                    # Older Telegram updates may omit chat_id; use the
                    # existing group-call cache rather than crashing.
                    chat_id = self._cache.get_chat_id(update.call.id)
                if chat_id is None:
                    return"""
if new in source:
    print("Compatibility patch already present")
elif old in source:
    target.write_text(source.replace(old, new, 1), encoding="utf-8")
    print("Applied UpdateGroupCall compatibility patch")
else:
    raise SystemExit("Unrecognized PyTgCalls source; patch not applied")
