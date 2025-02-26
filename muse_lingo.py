import random
import json
import os
import argparse
from typing import Dict, List, Tuple, Optional

# MuseLingo: A Multilingual Poetry Generator
# This application generates poetry in multiple languages based on themes and emotions
# It can also translate poetry between languages while attempting to preserve poetic qualities

class MuseLingo:
    def __init__(self, data_path: str = "poetry_data.json"):
        """Initialize the MuseLingo poetry generator with language data."""
        self.languages = ["english", "spanish", "french", "japanese", "arabic"]
        self.themes = ["love", "nature", "time", "freedom", "sorrow", "hope"]
        self.emotions = ["joy", "melancholy", "wonder", "longing", "serenity"]
        self.poetry_forms = ["haiku", "sonnet", "free_verse", "quatrain", "tanka"]
        
        # Load language data if file exists, otherwise create default data
        if os.path.exists(data_path):
            with open(data_path, 'r', encoding='utf-8') as f:
                self.language_data = json.load(f)
        else:
            self.language_data = self._create_default_data()
            with open(data_path, 'w', encoding='utf-8') as f:
                json.dump(self.language_data, f, ensure_ascii=False, indent=2)
    
    def _create_default_data(self) -> Dict:
        """Create default language data structures if no data file is found."""
        data = {}
        
        # English
        data["english"] = {
            "words": {
                "love": ["love", "heart", "soul", "embrace", "adore", "cherish", "passion"],
                "nature": ["tree", "river", "mountain", "flower", "ocean", "forest", "sky"],
                "time": ["moment", "eternity", "hour", "memory", "age", "season", "decade"],
                "freedom": ["wings", "horizon", "unbounded", "soar", "limitless", "choice", "liberty"],
                "sorrow": ["tears", "shadow", "loss", "grief", "abyss", "hollow", "void"],
                "hope": ["light", "dawn", "horizon", "promise", "seed", "tomorrow", "dream"]
            },
            "emotions": {
                "joy": ["bright", "dancing", "radiant", "laughing", "vibrant", "golden", "sparkling"],
                "melancholy": ["fading", "distant", "somber", "gray", "gentle", "quiet", "lingering"],
                "wonder": ["vast", "mysterious", "starlit", "infinite", "magical", "breathless", "awestruck"],
                "longing": ["yearning", "reaching", "remembering", "distant", "calling", "seeking", "awaiting"],
                "serenity": ["still", "peaceful", "calm", "tranquil", "flowing", "balanced", "harmonious"]
            },
            "structures": {
                "haiku": ["5-7-5 syllables", "nature reference", "seasonal element"],
                "sonnet": ["14 lines", "iambic pentameter", "volta after octave"],
                "free_verse": ["varied rhythm", "no fixed pattern", "natural pauses"],
                "quatrain": ["four-line stanzas", "AABB or ABAB rhyme", "regular meter"],
                "tanka": ["5-7-5-7-7 syllables", "intense imagery", "turn in the third line"]
            },
            "connectors": ["and", "but", "when", "as", "like", "through", "beneath", "beyond", "within", "until"],
            "line_starters": ["I", "The", "A", "In", "When", "Like", "Through", "With", "Without", "Among"]
        }
        
        # Spanish
        data["spanish"] = {
            "words": {
                "love": ["amor", "corazón", "alma", "abrazar", "adorar", "querer", "pasión"],
                "nature": ["árbol", "río", "montaña", "flor", "océano", "bosque", "cielo"],
                "time": ["momento", "eternidad", "hora", "memoria", "edad", "estación", "década"],
                "freedom": ["alas", "horizonte", "sin límites", "volar", "infinito", "elección", "libertad"],
                "sorrow": ["lágrimas", "sombra", "pérdida", "dolor", "abismo", "vacío", "ausencia"],
                "hope": ["luz", "amanecer", "horizonte", "promesa", "semilla", "mañana", "sueño"]
            },
            "emotions": {
                "joy": ["brillante", "bailando", "radiante", "riendo", "vibrante", "dorado", "resplandeciente"],
                "melancholy": ["desvaneciendo", "distante", "sombrío", "gris", "suave", "quieto", "persistente"],
                "wonder": ["vasto", "misterioso", "estrellado", "infinito", "mágico", "maravillado", "asombrado"],
                "longing": ["añorando", "alcanzando", "recordando", "distante", "llamando", "buscando", "esperando"],
                "serenity": ["inmóvil", "pacífico", "calmo", "tranquilo", "fluyendo", "equilibrado", "armonioso"]
            },
            "structures": {
                "haiku": ["5-7-5 sílabas", "referencia a la naturaleza", "elemento estacional"],
                "sonnet": ["14 líneas", "endecasílabos", "vuelta después del octavo verso"],
                "free_verse": ["ritmo variado", "sin patrón fijo", "pausas naturales"],
                "quatrain": ["estrofas de cuatro líneas", "rima AABB o ABAB", "metro regular"],
                "tanka": ["5-7-5-7-7 sílabas", "imágenes intensas", "giro en la tercera línea"]
            },
            "connectors": ["y", "pero", "cuando", "como", "cual", "por", "bajo", "más allá", "dentro", "hasta"],
            "line_starters": ["Yo", "El", "La", "En", "Cuando", "Como", "A través", "Con", "Sin", "Entre"]
        }
        
        # French
        data["french"] = {
            "words": {
                "love": ["amour", "cœur", "âme", "étreinte", "adorer", "chérir", "passion"],
                "nature": ["arbre", "rivière", "montagne", "fleur", "océan", "forêt", "ciel"],
                "time": ["moment", "éternité", "heure", "mémoire", "âge", "saison", "décennie"],
                "freedom": ["ailes", "horizon", "sans bornes", "s'envoler", "illimité", "choix", "liberté"],
                "sorrow": ["larmes", "ombre", "perte", "chagrin", "abîme", "vide", "creux"],
                "hope": ["lumière", "aube", "horizon", "promesse", "graine", "demain", "rêve"]
            },
            "emotions": {
                "joy": ["brillant", "dansant", "radieux", "riant", "vibrant", "doré", "étincelant"],
                "melancholy": ["s'évanouissant", "lointain", "sombre", "gris", "doux", "calme", "persistant"],
                "wonder": ["vaste", "mystérieux", "étoilé", "infini", "magique", "émerveillé", "stupéfait"],
                "longing": ["aspirant", "atteignant", "se souvenant", "distant", "appelant", "cherchant", "attendant"],
                "serenity": ["immobile", "paisible", "calme", "tranquille", "fluide", "équilibré", "harmonieux"]
            },
            "structures": {
                "haiku": ["5-7-5 syllabes", "référence à la nature", "élément saisonnier"],
                "sonnet": ["14 lignes", "alexandrins", "volta après l'octave"],
                "free_verse": ["rythme varié", "sans forme fixe", "pauses naturelles"],
                "quatrain": ["strophes de quatre lignes", "rime AABB ou ABAB", "mètre régulier"],
                "tanka": ["5-7-5-7-7 syllabes", "imagerie intense", "tournant à la troisième ligne"]
            },
            "connectors": ["et", "mais", "quand", "comme", "tel", "à travers", "sous", "au-delà", "dans", "jusqu'à"],
            "line_starters": ["Je", "Le", "La", "Dans", "Quand", "Comme", "À travers", "Avec", "Sans", "Parmi"]
        }
        
        # Japanese
        data["japanese"] = {
            "words": {
                "love": ["愛", "心", "魂", "抱擁", "崇拝", "大切", "情熱"],
                "nature": ["木", "川", "山", "花", "海", "森", "空"],
                "time": ["瞬間", "永遠", "時間", "記憶", "年齢", "季節", "十年"],
                "freedom": ["翼", "地平線", "無限", "飛翔", "無制限", "選択", "自由"],
                "sorrow": ["涙", "影", "喪失", "悲嘆", "深淵", "虚無", "空虚"],
                "hope": ["光", "夜明け", "地平線", "約束", "種", "明日", "夢"]
            },
            "emotions": {
                "joy": ["明るい", "踊る", "輝く", "笑う", "鮮やか", "黄金", "きらめく"],
                "melancholy": ["薄れゆく", "遠い", "物悲しい", "灰色", "優しい", "静か", "長引く"],
                "wonder": ["広大", "神秘的", "星空", "無限", "魔法のような", "息をのむ", "畏敬"],
                "longing": ["憧れ", "手を伸ばす", "思い出す", "遠い", "呼びかける", "探し求める", "待つ"],
                "serenity": ["静止", "平和", "穏やか", "静穏", "流れる", "均衡", "調和"]
            },
            "structures": {
                "haiku": ["5-7-5音節", "自然への言及", "季節の要素"],
                "sonnet": ["14行", "特定のリズム", "8行目後の転換"],
                "free_verse": ["変化するリズム", "固定パターンなし", "自然な休止"],
                "quatrain": ["4行の詩節", "特定の韻律パターン", "規則的なメーター"],
                "tanka": ["5-7-5-7-7音節", "強烈なイメージ", "3行目での転換"]
            },
            "connectors": ["と", "しかし", "時", "よう", "のような", "通して", "下", "超えて", "中", "まで"],
            "line_starters": ["私は", "その", "一つの", "で", "時", "のよう", "通して", "と", "無し", "の中"]
        }
        
        # Arabic
        data["arabic"] = {
            "words": {
                "love": ["حب", "قلب", "روح", "عناق", "عبادة", "تقدير", "شغف"],
                "nature": ["شجرة", "نهر", "جبل", "زهرة", "محيط", "غابة", "سماء"],
                "time": ["لحظة", "أبدية", "ساعة", "ذاكرة", "عمر", "موسم", "عقد"],
                "freedom": ["أجنحة", "أفق", "لا حدود", "تحليق", "لا حد", "اختيار", "حرية"],
                "sorrow": ["دموع", "ظل", "فقدان", "حزن", "هاوية", "فراغ", "خواء"],
                "hope": ["نور", "فجر", "أفق", "وعد", "بذرة", "غد", "حلم"]
            },
            "emotions": {
                "joy": ["مشرق", "راقص", "متألق", "ضاحك", "نابض", "ذهبي", "متلألئ"],
                "melancholy": ["متلاشي", "بعيد", "كئيب", "رمادي", "لطيف", "هادئ", "مستمر"],
                "wonder": ["شاسع", "غامض", "مرصع بالنجوم", "لا نهائي", "سحري", "مذهل", "مندهش"],
                "longing": ["شوق", "وصول", "تذكر", "بعيد", "نداء", "بحث", "انتظار"],
                "serenity": ["ساكن", "مسالم", "هادئ", "صافي", "متدفق", "متوازن", "متناغم"]
            },
            "structures": {
                "haiku": ["5-7-5 مقاطع", "إشارة للطبيعة", "عنصر موسمي"],
                "sonnet": ["14 سطرًا", "إيقاع معين", "تحول بعد البيت الثامن"],
                "free_verse": ["إيقاع متنوع", "بدون نمط ثابت", "توقفات طبيعية"],
                "quatrain": ["مقاطع من أربعة أسطر", "قافية معينة", "وزن منتظم"],
                "tanka": ["5-7-5-7-7 مقاطع", "صور قوية", "تحول في السطر الثالث"]
            },
            "connectors": ["و", "لكن", "عندما", "مثل", "كـ", "عبر", "تحت", "وراء", "داخل", "حتى"],
            "line_starters": ["أنا", "الـ", "واحد", "في", "عندما", "مثل", "عبر", "مع", "بدون", "بين"]
        }
        
        return data

    def generate_poem(self, language: str, theme: str, emotion: str, form: str, 
                     lines: int = 6, translator: Optional[Dict] = None) -> List[str]:
        """Generate a poem in the specified language, theme, emotion, and form."""
        if language not in self.languages:
            raise ValueError(f"Language '{language}' not supported. Choose from: {', '.join(self.languages)}")
        if theme not in self.themes:
            raise ValueError(f"Theme '{theme}' not supported. Choose from: {', '.join(self.themes)}")
        if emotion not in self.emotions:
            raise ValueError(f"Emotion '{emotion}' not supported. Choose from: {', '.join(self.emotions)}")
        if form not in self.poetry_forms:
            raise ValueError(f"Form '{form}' not supported. Choose from: {', '.join(self.poetry_forms)}")
        
        language_data = self.language_data[language]
        
        # Select words based on theme and emotion
        theme_words = language_data["words"][theme]
        emotion_words = language_data["emotions"][emotion]
        connectors = language_data["connectors"]
        starters = language_data["line_starters"]
        
        poem = []
        
        # Adjust generation strategy based on form
        if form == "haiku":
            poem = self._generate_haiku(language, theme_words, emotion_words)
        elif form == "tanka":
            poem = self._generate_tanka(language, theme_words, emotion_words)
        else:
            # Generic poem generation for other forms
            for i in range(lines):
                if i == 0 or random.random() < 0.3:  # 30% chance to start with a line starter
                    line = random.choice(starters)
                    
                    # Add theme or emotion word
                    if random.random() < 0.5:
                        line += " " + random.choice(theme_words)
                    else:
                        line += " " + random.choice(emotion_words)
                    
                    # Add a connector sometimes
                    if random.random() < 0.3:
                        line += " " + random.choice(connectors)
                    
                    # Add another word
                    if random.random() < 0.5:
                        line += " " + random.choice(theme_words)
                    else:
                        line += " " + random.choice(emotion_words)
                else:
                    # More varied line construction
                    if random.random() < 0.5:
                        line = random.choice(theme_words) + " " + random.choice(connectors) + " " + random.choice(emotion_words)
                    else:
                        line = random.choice(emotion_words) + " " + random.choice(theme_words)
                
                # Capitalize first letter and add punctuation occasionally
                line = line[0].upper() + line[1:]
                if random.random() < 0.3 and i < lines - 1:
                    line += random.choice([",", "...", ";", "—"])
                elif i == lines - 1:
                    line += random.choice([".", "...", "!"])
                
                poem.append(line)
        
        # Translate if a translator is provided
        if translator:
            translated_poem = []
            for line in poem:
                translated_line = ""
                words = line.split()
                for word in words:
                    # Strip punctuation for translation
                    punctuation = ""
                    if word[-1] in ",.;!?—":
                        punctuation = word[-1]
                        word = word[:-1]
                    
                    # Try to translate the word
                    if word.lower() in translator:
                        translated_word = translator[word.lower()]
                        # Preserve capitalization
                        if word[0].isupper():
                            translated_word = translated_word[0].upper() + translated_word[1:]
                        translated_line += translated_word + punctuation + " "
                    else:
                        translated_line += word + punctuation + " "
                
                translated_poem.append(translated_line.strip())
            return translated_poem
        
        return poem

    def _generate_haiku(self, language: str, theme_words: List[str], emotion_words: List[str]) -> List[str]:
        """Generate a haiku poem (5-7-5 syllable pattern)."""
        # This is a simplified approach - for a real implementation,
        # we would need syllable counting specific to each language
        haiku = []
        
        # First line (5 syllables)
        haiku.append(random.choice(theme_words).capitalize())
        
        # Second line (7 syllables)
        second_line = random.choice(emotion_words) + " " + random.choice(theme_words)
        haiku.append(second_line)
        
        # Third line (5 syllables)
        haiku.append(random.choice(emotion_words))
        
        return haiku

    def _generate_tanka(self, language: str, theme_words: List[str], emotion_words: List[str]) -> List[str]:
        """Generate a tanka poem (5-7-5-7-7 syllable pattern)."""
        # Start with a haiku
        tanka = self._generate_haiku(language, theme_words, emotion_words)
        
        # Add two more lines (7 syllables each)
        connectors = self.language_data[language]["connectors"]
        
        # Fourth line
        fourth_line = random.choice(emotion_words) + " " + random.choice(connectors) + " " + random.choice(theme_words)
        tanka.append(fourth_line)
        
        # Fifth line
        fifth_line = random.choice(theme_words) + " " + random.choice(emotion_words)
        tanka.append(fifth_line)
        
        return tanka

    def build_translator(self, source_lang: str, target_lang: str) -> Dict:
        """Build a simple word-to-word translator between two languages."""
        if source_lang not in self.languages or target_lang not in self.languages:
            raise ValueError(f"Both languages must be one of: {', '.join(self.languages)}")
        
        translator = {}
        source_data = self.language_data[source_lang]
        target_data = self.language_data[target_lang]
        
        # Map theme words
        for theme in self.themes:
            source_words = source_data["words"][theme]
            target_words = target_data["words"][theme]
            
            # Match words by position
            for i in range(min(len(source_words), len(target_words))):
                translator[source_words[i]] = target_words[i]
        
        # Map emotion words
        for emotion in self.emotions:
            source_words = source_data["emotions"][emotion]
            target_words = target_data["emotions"][emotion]
            
            # Match words by position
            for i in range(min(len(source_words), len(target_words))):
                translator[source_words[i]] = target_words[i]
        
        # Map connectors
        source_connectors = source_data["connectors"]
        target_connectors = target_data["connectors"]
        for i in range(min(len(source_connectors), len(target_connectors))):
            translator[source_connectors[i]] = target_connectors[i]
        
        # Map line starters
        source_starters = source_data["line_starters"]
        target_starters = target_data["line_starters"]
        for i in range(min(len(source_starters), len(target_starters))):
            translator[source_starters[i]] = target_starters[i]
            
        return translator

    def add_vocabulary(self, language: str, theme: str, words: List[str]) -> None:
        """Add new vocabulary words to a language theme."""
        if language not in self.languages:
            raise ValueError(f"Language '{language}' not supported")
        if theme not in self.themes:
            raise ValueError(f"Theme '{theme}' not supported")
        
        self.language_data[language]["words"][theme].extend(words)
    
    def save_language_data(self, file_path: str = "poetry_data.json") -> None:
        """Save the current language data to a JSON file."""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.language_data, f, ensure_ascii=False, indent=2)
    
    def get_available_languages(self) -> List[str]:
        """Get a list of all available languages."""
        return self.languages
    
    def get_available_themes(self) -> List[str]:
        """Get a list of all available themes."""
        return self.themes
    
    def get_available_emotions(self) -> List[str]:
        """Get a list of all available emotions."""
        return self.emotions
    
    def get_available_forms(self) -> List[str]:
        """Get a list of all available poetry forms."""
        return self.poetry_forms


def main():
    """Main function to run the MuseLingo poetry generator from command line."""
    parser = argparse.ArgumentParser(description="MuseLingo: Multilingual Poetry Generator")
    parser.add_argument("--language", "-l", type=str, default="english",
                        help="Language for the poem (english, spanish, french, japanese, arabic)")
    parser.add_argument("--theme", "-t", type=str, default="love",
                        help="Theme of the poem (love, nature, time, freedom, sorrow, hope)")
    parser.add_argument("--emotion", "-e", type=str, default="joy",
                        help="Emotional tone (joy, melancholy, wonder, longing, serenity)")
    parser.add_argument("--form", "-f", type=str, default="free_verse",
                        help="Poetry form (haiku, sonnet, free_verse, quatrain, tanka)")
    parser.add_argument("--lines", "-n", type=int, default=6,
                        help="Number of lines (for forms other than haiku and tanka)")
    parser.add_argument("--translate", "-tr", type=str, default=None,
                        help="Translate to this language")
    
    args = parser.parse_args()
    
    try:
        muse = MuseLingo()
        
        # Print available options
        print("MuseLingo: A Multilingual Poetry Generator")
        print(f"Languages: {', '.join(muse.get_available_languages())}")
        print(f"Themes: {', '.join(muse.get_available_themes())}")
        print(f"Emotions: {', '.join(muse.get_available_emotions())}")
        print(f"Forms: {', '.join(muse.get_available_forms())}")
        print()
        
        print(f"Generating a {args.form} in {args.language} about {args.theme} with a {args.emotion} tone:")
        print("=" * 50)
        
        translator = None
        if args.translate:
            translator = muse.build_translator(args.language, args.translate)
            print(f"(With translation to {args.translate})")
        
        poem = muse.generate_poem(args.language, args.theme, args.emotion, 
                                  args.form, args.lines, translator)
        
        for line in poem:
            print(line)
            
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()