language = input("Enter a language (e.g. Spanish, French, Japanese): ").strip().lower()
translations = {
    "english": "Hello World!",
    "spanish": "¡Hola Mundo!",
    "french": "Bonjour le monde!",
    "german": "Hallo Welt!",
    "italian": "Ciao mondo!",
    "portuguese": "Olá Mundo!",
    "japanese": "こんにちは世界！",
    "chinese": "你好，世界！",
    "korean": "안녕하세요 세계!",
    "russian": "Привет, мир!",
}

print(translations.get(language, "Hello World!"))
