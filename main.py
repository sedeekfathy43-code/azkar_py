from pywebio.input import *
from pywebio.output import *
from pywebio import start_server

def app():
    put_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxDKHhPwre6aIxrcmuRq6kWDfhk-JeODAw_w&s' ,width='900p' , height='300p')
    put_html("""<h3 id='h3'> تطبيق  اذكار الصباح والمساء</h3>
        <p id='para'> اهلا وسهلا بكم في تطبيقنا الجديد لقرأة الاذكار  </p>

        <ul>
            
            
        <details style="direction: rtl; text-align: right; margin-top: 10px;">
            <summary style="cursor: pointer; font-weight: bold; color: #ffd700;">☀️ أذكار الصباح (اضغط للعرض)</summary>
            <div style="padding: 10px; background: #333; border-radius: 5px; margin-top: 5px;">
                <p>• أصبحنا وأصبح الملك لله والحمد لله.</p>
                <p>•    للَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ ۚ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ ۗ مَن ذَا الَّذِي يَشْفَعُ عِندَهُ إِلَّا بِإِذْنِهِ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلَّا بِمَا شَاءَ ۚ وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ ۖ وَلَا يَئُودُهُ حِفْظُهُمَا ۚ وَهُوَ الْعَلِيُّ
 الْعَظِيم</p> 
                <p>• اللهم بك أصبحنا وبك أمسينا وبك نحيا وبك نموت وإليك النشور.</p>
            </div>
        </details>

        <details style="direction: rtl; text-align: right; margin-top: 10px;">
            <summary style="cursor: pointer; font-weight: bold; color: #ffd700;">🌙 أذكار المساء (اضغط للعرض)</summary>
            <div style="padding: 10px; background: #333; border-radius: 5px; margin-top: 5px;">
                <p>• أمسينا وأمسى الملك لله والحمد لله.</p>
                <p>• اللهم بك أمسينا وبك أصبحنا وبك نحيا وبك نموت وإليك المصير.</p>
                <p>• أعوذ بكلمات الله التامات من شر ما خلق.</p>
            </div>
        </details>
        <hr>
        <p>جميع الحقوق محفوظة للمطور @ صديق فتحى</p>     
    """ ) 
    
if __name__ == '__main__':
    start_server(app, port=8080, host='0.0.0.0') 