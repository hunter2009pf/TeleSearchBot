from actions.interact_with_llm import KimiChat


class LLMManager:
    kimi_client_map = {}

    @classmethod
    def create_kimi_client(cls, session_id: int) -> KimiChat:
        temp = KimiChat(session_id=session_id)
        LLMManager.kimi_client_map[session_id] = temp
        return temp
