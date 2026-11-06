[English](../1-install.md)

<div dir="rtl" lang="he">

# שלב 1 - התקנת OrcaSlicer

מדפסת תלת-ממד לא יודעת לקרוא מודל תלת-ממדי ישירות. **סלייסר** (slicer) הוא תוכנה שחותכת את המודל לשכבות דקות, והופכת אותן להוראות שהמדפסת מבינה (קובץ ‎`.gcode`). במדריך הזה משתמשים ב-**OrcaSlicer**. היא חינמית, עובדת על Windows, Mac ו-Linux, והדפסות הבדיקה כבר מובנות בה.

השתמשו בגרסה **2.4.2** (הגרסה היציבה הנוכחית). גם 2.5.0 עובדת.

## הורדה

1. היכנסו ל[עמוד ההורדה של OrcaSlicer 2.4.2](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/v2.4.2).
2. גללו למטה עד **Assets**.
3. לחצו על הקובץ שמתאים למחשב שלכם:

| המחשב שלכם | הקובץ להורדה |
|---|---|
| Windows (כמעט כל המחשבים) | `OrcaSlicer_Windows_Installer_V2.4.2_x64.exe` |
| Windows על ARM (למשל Surface Pro X, מחשבים ניידים עם Snapdragon) | `OrcaSlicer_Windows_Installer_V2.4.2_arm64.exe` |
| Mac (Intel או Apple M1/M2/M3/M4) | `OrcaSlicer_Mac_universal_V2.4.2.dmg` |
| Linux | `OrcaSlicer_Linux_AppImage_Ubuntu2404_V2.4.2.AppImage` |

את שאר הקבצים בעמוד לא צריך.

## התקנה

### Windows

1. לחצו לחיצה כפולה על קובץ ה-‎`.exe` שהורדתם.
2. אולי תופיע תיבה כחולה עם הכיתוב **"Windows protected your PC"‎**. אם כן, לחצו על **More info** ואז על **Run anyway**. (התוכנה בטוחה. פשוט Microsoft לא חתמה עליה.)
3. לחצו כל הזמן **Next**, ובסוף **Finish**.
4. פתחו את **OrcaSlicer** מתפריט Start.

### Mac

1. לחצו לחיצה כפולה על קובץ ה-‎`.dmg` שהורדתם.
2. גררו את הסמל של **OrcaSlicer** אל התיקייה **Applications**.
3. פתחו את **Applications** ולחצו לחיצה כפולה על **OrcaSlicer**.
4. אולי macOS יגיד שאי אפשר לפתוח את התוכנה (**cannot be opened**) או שאי אפשר לאמת מי פיתח אותה (**can't verify the developer**). אם כן, פתחו את **System Settings → Privacy & Security**. גללו למטה ולחצו על **Open Anyway** ליד ההודעה על OrcaSlicer. הקלידו את הסיסמה שלכם כדי לאשר.

### Linux

1. לחצו לחיצה ימנית על קובץ ה-‎`.AppImage` שהורדתם, בחרו **Properties**, עברו ל-**Permissions** וסמנו **Allow executing file as program**.
2. לחצו עליו לחיצה כפולה.

## הפעלה ראשונה: מספרים ל-Orca איזו מדפסת יש לכם

בפעם הראשונה ש-OrcaSlicer נפתחת, מופיע **אשף הגדרה** (setup wizard). הוא שואל כמה שאלות, עמוד אחרי עמוד.

1. בעמוד **Login**: לחצו **Skip**. לא צריך חשבון.
2. בעמוד **Printer**: מצאו את היצרן של המדפסת (למשל **Creality**). סמנו את הדגם שלכם, למשל **Ender-3 Pro**, עם nozzle בגודל **0.4**. (ה-nozzle, או בעברית דיזה, הוא הקצה החם ממתכת שממנו יוצא הפלסטיק המותך.)
3. בעמוד **Filament**: ודאו ש-**Generic PLA** מסומן.
4. לחצו **Finish**.

פספסתם את האשף? אפשר להוסיף מדפסת גם אחר כך. לחצו על סמל גלגל השיניים ליד שם המדפסת (למעלה משמאל, בתיבה **Printer**).

השלב הבא: [שלב 2 - טעינת ההגדרות של הפרויקט](2-presets.md)

</div>
