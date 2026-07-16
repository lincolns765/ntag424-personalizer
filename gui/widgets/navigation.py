from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget


class Navigation(QListWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(220)

        self.addItems([
            "🏠 Dashboard",
            "📥 Ingestion",
            "🖼 Review Queue",
            "🗄 Database",
            "☁️ Cloudflare",
            "🤖 OpenAI",
            "📊 Analytics",
            "📜 Logs",
            "⚙️ Settings",
        ])

        self.setCurrentRow(0)