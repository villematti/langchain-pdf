from langchain.memory import ConversationBufferMemory
from app.chat.memories.histories.sql_history import SqlMessageHistory


def build_memory(chat_args):
    sqlMsg = SqlMessageHistory(
            conversation_id=chat_args.conversation_id
        )
    return ConversationBufferMemory(
        chat_memory=sqlMsg,
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )