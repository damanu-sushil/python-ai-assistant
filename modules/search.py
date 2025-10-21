from modules.talk import talk
import wikipedia
import webbrowser

def search_web(query: str) -> str:
    """
    Searches for a query:
    1️⃣ If the user explicitly asks to open Google → open Google.
    2️⃣ Otherwise → try Wikipedia first.
    3️⃣ If Wikipedia fails → open Google as fallback.
    Returns: short summary string or None.
    """
    query_lower = query.lower().strip()

    try:
        # --- If user explicitly says "open/search/google/go to" ---
        if any(word in query_lower for word in ["open google", "search in google", "search on google", "go to google"]) or query_lower.startswith("google "):
            search_term = query_lower.replace("google", "").replace("open", "").replace("search", "").replace("go to", "").strip()
            url = "https://www.google.com"
            if search_term:
                url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
            webbrowser.open(url)
            talk(f"Opening Google for {search_term or 'you'}.")
            return f"Opening Google for {search_term or 'you'}."

        # --- Try Wikipedia first ---
        wikipedia.set_lang("en")
        summary = wikipedia.summary(query, sentences=2, auto_suggest=True)
        talk("According to Wikipedia.")
        talk(summary)
        return summary

    except wikipedia.exceptions.DisambiguationError as e:
        msg = f"Your query '{query}' refers to multiple topics. Try: {', '.join(e.options[:3])}."
        talk(msg)
        return msg

    except wikipedia.exceptions.PageError:
        # --- Wikipedia page not found → fallback to Google ---
        talk(f"Couldn't find {query} on Wikipedia. Searching Google instead.")
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(url)
        return f"I couldn't find {query} on Wikipedia, so I opened Google."

    except Exception as e:
        print(f"Error: {e}")
        talk("Sorry, I couldn't complete the search.")
        return f"An error occurred while searching for {query}."
