from rag_chatbot import YouTubeRAGChatbot

chatbot = YouTubeRAGChatbot(
    "https://www.youtube.com/watch?v=VIDEO_ID"
)

while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        break

    result = chatbot.ask(query)
    print("\nAnswer:\n", result["answer"])

