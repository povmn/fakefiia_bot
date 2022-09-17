import os
import ftp


def index(id, name, date):
    try:
        os.system('mkdir tmp')
    except:
        pass
    with open(f"tmp/{id}.html", mode="w") as f:
        f.write(f"""


	<!DOCTYPE html>
	<html lang="ru" dir="ltr">
	   <head>
	      <meta charset="utf-8">
	      <meta name="apple-mobile-web-app-capable" content="yes">
	      <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
	      <link rel="icon" type="image/png" href="access/favicon.png">
	      <meta name="apple-mobile-web-app-status-bar-style" content="black">
	      <link rel="apple-touch-icon-precomposed" href="access/favicon.png" />
	      <!-- <link rel="manifest" href="nediya.webmanifest"> -->
	      <link rel="manifest" href="manifest.json">
	      <meta name="apple-mobile-web-app-title" content="Дія">

	      <link rel="stylesheet" href="access/main.css?28977925" type="text/css">
	      <link rel="stylesheet" href="https://kit-pro.fontawesome.com/releases/v5.15.3/css/pro.min.css" type="text/css">
	      <title>Дія</title>
	   </head>
	   <body>
	      <div class="loadpage">
	         <div style="display:none" class="diyalogo"></div>
	         <div style="display:none" class="zublogo"></div>
	         <div style="display:none" class="loadtext">Міністерство<br>цифрової трансформації<br>України</div>
	      </div>
	      <div class="loginpage" style="display:none">
	         <div class="login_title">Код для входу</div>

	         <div class="keyboard">
	           <div class="cricles">
	              <div class="dot"></div>
	              <div class="dot"></div>
	              <div class="dot"></div>
	              <div class="dot"></div>
	           </div>

	           <br>

	            <div class="key r25" onclick="buttonclick(1)">
	               <span>1</span>
	            </div>
	            <div class="key r25" onclick="buttonclick(2)">
	               <span>2</span>
	            </div>
	            <div class="key" onclick="buttonclick(3)">
	               <span>3</span>
	            </div>
	            <div class="key r25 t10" onclick="buttonclick(4)">
	               <span>4</span>
	            </div>
	            <div class="key r25 t10" onclick="buttonclick(5)">
	               <span>5</span>
	            </div>
	            <div class="key t10" onclick="buttonclick(6)">
	               <span>6</span>
	            </div>
	            <div class="key r25 t10" onclick="buttonclick(7)">
	               <span>7</span>
	            </div>
	            <div class="key r25 t10" onclick="buttonclick(8)">
	               <span>8</span>
	            </div>
	            <div class="key t10" onclick="buttonclick(9)">
	               <span>9</span>
	            </div>
	            <div class="fastauth eblo r25 t10" onclick="buttonclick(98)">
	               <span>-</span>
	            </div>
	            <div class="key r25 t10" onclick="buttonclick(0)">
	               <span>0</span>
	            </div>
	            <div class="key krest t10" onclick="buttonclick(99)">
	               <span>-</span>
	            </div>
	         </div>
	         <div class="login_footer">Не пам'ятаю код для входу</div>
	      </div>
	      <div class="menulid"  style="display: none">
	         <div class="header">
	            <div class="logos">
	               <div class="diya">
					  <!-- #ФИО #toedit -->
	                  <div class="pathtitle menutitile">Вітаємо, Роман</div>
	                  <!---->
	               </div>
	               <div class="scanqr"></div>
	            </div>
	         </div>
	         <div class="mainpage">
	            <div class="menu">
	               <div class="menulist sos">
	                  <span>
	                     <div></div>
	                     Дія.Підпис
	                  </span>
	               </div>
	               <div class="zaz menulist sos">
	                  <span>
	                     <div></div>
	                     Підключені пристрої
	                  </span>
	               </div>
	               <div class="menulist sos">
	                  <span>
	                     <div></div>
	                     Функції та підказки
	                  </span>
	               </div>
	               <div class="menulist sos">
	                  <span>
	                     <div></div>
	                     Питання та відповіді
	                  </span>
	               </div>
	               <div class="zaz menulist sos">
	                  <span>
	                     <div></div>
	                     Служба підтримки
	                  </span>
	               </div>
	               <div class="menulist sos">
	                  <span>
	                     <div></div>
	                     Копіювати номер пристрою
	                  </span>
	               </div>
	               <div class="zaz menulist sos">
	                  <span>
	                     <div></div>
	                     Налаштування
	                  </span>
	               </div>
	               <div class="menulist sos">
	                  <span>
	                     <div></div>
	                     Про Дію
	                  </span>
	               </div>
	               <div class="menulist sos">
	                  <span>
	                     <div></div>
	                     Розповісти друзям
	                  </span>
	               </div>
	               <div class="zaz menulist sos">
	                  <span>
	                     <div></div>
	                     Оцінити застосунок
	                  </span>
	               </div>
	               <div class="menulist sos">
	                  <span>
	                     <div></div>
	                     Вийти
	                  </span>
	               </div>
	            </div>
	         </div>
	         <div class="footer zep">
	            <div class="ft_icons">
	               <div class="icon doc">
	                  <div class="ico"></div>
	                  Документи
	               </div>
	               <div class="icon pos">
	                  <div class="ico"></div>
	                  Послуги
	               </div>
	               <div class="icon pov">
	                  <div class="ico"></div>
	                  Повідомлення
	               </div>
	               <div class="icon men act">
	                  <div class="ico"></div>
	                  Меню
	               </div>
	            </div>
	         </div>
	      </div>
	      <div class="poslugi" style="display: none">
	         <div class="header">
	            <div class="logos">
	               <div class="diya">
	                  <div class="pathtitle">Послуги</div>
	               </div>
	               <div class="scanqr"></div>
	            </div>
	         </div>
	         <div class="mainpage">
	            <div class="menu">
	               <div class="menulist">
	                  <span>Виконавчі провадження</span>
	                  <div class="arrow"></div>
	               </div>
	               <div class="menulist">
	                  <span>Штрафи за порушення ПДР</span>
	                  <div class="arrow"></div>
	               </div>
	               <div class="cov menulist">
	                  <span>COVID-сертифікати</span>
	                  <div>В розробці</div>
	               </div>
	               <div class="menulist">
	                  <span>Одноразова допомога ФОПам та найманим працівникам</span>
	                  <div class="arrow"></div>
	               </div>
	               <div class="menulist">
	                  <span>Заміна посвідчення водія</span>
	                  <div class="arrow"></div>
	               </div>
	               <div class="menulist">
	                  <span>Петиції</span>
	                  <div class="arrow"></div>
	               </div>
	               <div class="menulist">
	                  <span>Сплата послуг за QR-кодом</span>
	                  <div class="arrow"></div>
	               </div>
	               <div class="menulist">
	                  <span>Реєстрація мiсця проживання</span>
	                  <div class="arrow"></div>
	               </div>
	               <div class="menulist">
	                  <span>Податкові послуги</span>
	                  <div class="arrow"></div>
	               </div>
	            </div>
	         </div>
	         <div class="footer zep">
	            <div class="ft_icons">
	               <div class="icon doc">
	                  <div class="ico"></div>
	                  Документи
	               </div>
	               <div class="icon pos">
	                  <div class="ico"></div>
	                  Послуги
	               </div>
	               <div class="icon pov act">
	                  <div class="ico"></div>
	                  Повідомлення
	               </div>
	               <div class="icon men">
	                  <div class="ico"></div>
	                  Меню
	               </div>
	            </div>
	         </div>
	      </div>
	      <div class="notifications" style="display: none">
	         <div class="header">
	            <div class="logos">
	               <div class="diya">
	                  <div class="pathtitle">Повідомлення</div>
	               </div>
	            </div>
	         </div>
	         <div class="mainpage">
	            <div class="ok">
	               <div class="okimg"></div>
	               У вас немає нових повідомлень.
	            </div>
	         </div>
	         <div class="footer zep">
	            <div class="ft_icons">
	               <div class="icon doc">
	                  <div class="ico"></div>
	                  Документи
	               </div>
	               <div class="icon pos">
	                  <div class="ico"></div>
	                  Послуги
	               </div>
	               <div class="icon pov act">
	                  <div class="ico"></div>
	                  Повідомлення
	               </div>
	               <div class="icon men">
	                  <div class="ico"></div>
	                  Меню
	               </div>
	            </div>
	         </div>
	      </div>
	      <div class="mainpage papage" style="opacity: 0">
	         <div class="header">
	            <div class="logos">
	               <div class="diya"></div>
	               <div class="scanqr"></div>
	            </div>
	         </div>
	         <div class="swiper-container">
	            <div class="swiper-wrapper">
	               <div class="swiper-slide passport pssprt">
	                  <div class="content front">
	                     <div class="ps_title">
	                        <div class="glav">Паспорт громадянина України</div>
	                        <div class="gerb"></div>
	                     </div>
	                     <div class="information">
	                     	<!-- #фото -->
	                        <div class="image" style="background-image: url(photo/{id}.jpg);"></div>
	                        <!---->
	                        <div class="info">
	                           <div class="opis">
	                           	  <!-- #дата #toedit -->
	                              <div class="date">Дата народження: {date}</div>
	                              <!---->
	                              <!-- #номерпаспорта #toedit -->
	                              <div class="number">Номер: 004216206</div>
	                              <!---->
				      			  <!-- #подпись -->
	                              <div style="background-image: url(sign.png);" class="sign"></div>
				                  <!---->
	                           </div>
	                        </div>
	                     </div>
	                     <div class="razdel"></div>
	                     <!-- #ФИО #toedit -->
	                     <div class="name">{name}</div>
	                     <!---->
	                     <div class="more"></div>
	                  </div>
	                  <div class="content back">
	                     <div class="loaded" style="opacity:0">
	                        <div class="qr_body">
	                           <div class="qr_title">QR КОД ДIЯТИМЕ 3 ХВ</div>
	                           <div class="qrcode"></div>
	                        </div>
	                        <div class="qrbuttons">
	                           <div class="qricon act"></div>
	                           <div class="shicon"></div>
	                        </div>
	                     </div>
	                     <div class="unloaded">
	                        <div class="loader_line"></div>
	                        <div class="glav">Паспорт громадянина України</div>
	                        <div class="qr_title">Завантаження...</div>
	                     </div>
	                  </div>
	               </div>
	               <div class="swiper-slide passport nlgi">
	                  <div class="platnik content front">
	                     <div class="ps_title">
	                        <div class="glav">Картка платника податків</div>
	                     </div>
	                     <div class="ps_deskr">
	                        <div class="deskr">PHOKПП</div>
	                     </div>
	                     <!-- #ФИО #toedit -->
	                     <div class="name">{name}</div>
	                     <!---->
	                     <!-- #дата #toedit -->
	                     <div class="date">Дата народження: {date}</div>
	                     <!---->
	                     <div class="line marquee">РНОКПП дійсний. Перевірено Державною податковою службою.</div>
	                     <!-- #ИНН #ІПН #toedit -->
	                     <div class="number">3857109110</div>
	                     <!---->
	                  </div>
	                  <div class="content back">
	                     <div class="loaded" style="opacity:0">
	                        <div class="qr_body">
	                           <div class="qr_title">QR КОД ДІЯТИМЕ 3 ХВ</div>
	                           <div class="qrcode"></div>
	                        </div>
	                        <div class="qrbuttons">
	                           <div class="qricon act"></div>
	                           <div class="shicon"></div>
	                        </div>
	                     </div>
	                     <div class="unloaded">
	                        <div class="loader_line"></div>
	                        <div class="glav">Картка платника податків</div>
	                        <div class="qr_title">Завантаження...</div>
	                     </div>
	                  </div>
	               </div>
	               <div class="swiper-slide passport svdtstv">
	                  <div class="content front">
	                     <div class="ps_title">
	                        <div class="rodi">Додати свідоцтво про народження дитини</div>
	                     </div>
	                     <div class="ps_deskr">
	                        <div class="rod_deskr">Зараз ви можете додати до документiв у Дії свідоцтво про народження своєї дитини. Для цього потрібні серія та номер свідоцтва.</div>
	                     </div>
	                     <div class="ps_deskr">
	                        <div class="rod_deskr">Інші документи наразі додати неможливо.</div>
	                     </div>
	                     <div class="rod_but">
	                        <span>Додати</span>
	                     </div>
	                  </div>
	                  <div class="content back">
	                     <div class="loaded" style="opacity:0">
	                        <div class="qr_body">
	                           <div class="qr_title">QR КОД ДІЯТИМЕ 3 ХВ</div>
	                           <div class="qrcode"></div>
	                        </div>
	                        <div class="qrbuttons">
	                           <div class="qricon act"></div>
	                           <div class="shicon"></div>
	                        </div>
	                     </div>
	                     <div class="unloaded">
	                        <div class="loader_line"></div>
	                        <div class="glav">Паспорт громадянина України</div>
	                        <div class="qr_title">Завантаження...</div>
	                     </div>
	                  </div>
	               </div>
	            </div>
	         </div>
	         <div class="refresh">
	            <div class="rf_title">Завантаження...</div>
	            <div class="doba">
	               <div class="dit_dot act"></div>
	               <div class="dit_dot"></div>
	               <div class="dit_dot"></div>
	            </div>
	         </div>
	         <div class="footer">
	            <div class="ft_icons">
	               <div class="icon doc act">
	                  <div class="ico"></div>
	                  Документи
	               </div>
	               <div class="icon pos">
	                  <div class="ico"></div>
	                  Послуги
	               </div>
	               <div class="icon pov">
	                  <div class="ico"></div>
	                  Повідомлення
	               </div>
	               <div class="icon men">
	                  <div class="ico"></div>
	                  Меню
	               </div>
	            </div>
	         </div>
	      </div>
	      
	      <script>
	        let correctpass=-1;
	      </script>
	      <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.css" />
	      <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css" />
	      <script src="https://unpkg.com/swiper/swiper-bundle.js"></script>
	      <script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>
	      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	      <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/2.2.0/anime.js"></script>
	      <script src="https://cdn.jsdelivr.net/npm/jquery.marquee@1.6.0/jquery.marquee.min.js" type="text/javascript"></script>
	      <script src="access/main.js"></script>

	   </body>
	</html>

""")

ftp