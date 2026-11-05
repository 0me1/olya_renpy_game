"""Build the birthday teaser from the game's existing artwork. Requires python-pptx and Pillow."""
from pathlib import Path
from PIL import Image, ImageOps
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.oxml.xmlchemy import OxmlElement
import json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'downloads'; OUT.mkdir(exist_ok=True)
TMP=Path('/workspace/presentation_build'); TMP.mkdir(exist_ok=True)
G=ROOT/'game'; P=Presentation(); P.slide_width=12192000; P.slide_height=6858000
C='F8EEDB'; N='142238'; B='723349'; GOLD='D6B375'; boxes=[]
def u(v): return int(v*6350)
def rect(s,x,y,w,h,color,alpha=100):
 sh=s.shapes.add_shape(1,u(x),u(y),u(w),u(h)); sh.fill.solid(); sh.fill.fore_color.rgb=RGBColor.from_string(color); sh.line.fill.background()
 if alpha<100:
  a=OxmlElement('a:alpha'); a.set('val',str(alpha*1000)); sh.fill._xPr.solidFill.srgbClr.append(a)
 return sh
def text(s,txt,x,y,w,h,size=48,color=N,font='Arial',bold=False):
 assert 'ё' not in txt and 'Ё' not in txt
 assert x>=0 and y>=0 and x+w<=1921 and y+h<=1081,(txt,x,y,w,h)
 sh=s.shapes.add_textbox(u(x),u(y),u(w),u(h)); tf=sh.text_frame;tf.word_wrap=True
 tf.margin_left=tf.margin_right=tf.margin_top=tf.margin_bottom=0
 for i,line in enumerate(txt.split('\n')):
  p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.text=line;p.font.name=font;p.font.size=Pt(size/2);p.font.bold=bold;p.font.color.rgb=RGBColor.from_string(color);p.space_after=Pt(6)
 boxes.append({'slide':len(P.slides),'text':txt,'rect':[x,y,w,h]})
 return sh
def pic(s,path,x,y,w,h):
 im=Image.open(path); iw,ih=im.size
 sh=s.shapes.add_picture(str(path),u(x),u(y),u(w),u(h))
 # Native cropping, keeping image proportions.
 r=iw/ih; target=w/h
 if r>target: sh.crop_left=sh.crop_right=(1-target/r)/2
 else: sh.crop_top=sh.crop_bottom=(1-r/target)/2
 return sh
def bg(s,name):pic(s,G/'images/backgrounds'/f'{name}.png',0,0,1920,1080)
def sprite(s,key,cx,scale=1,y=0):
 return s.shapes.add_picture(str(G/'images_normalized/olya'/f'{key}.png'),u(cx-800*scale),u(y),u(1600*scale),u(1600*scale))
def slide(notes,color=C):
 s=P.slides.add_slide(P.slide_layouts[6]);s.background.fill.solid();s.background.fill.fore_color.rgb=RGBColor.from_string(color)
 assert not any(c in notes for c in 'ёЁ');s.notes_slide.notes_text_frame.text=notes;return s
def title(s,t,color=N,size=88):text(s,t,90,62,1750,140,size,color,'Georgia')
def panel(s,x,y,w,h,world='storybook',kind='dialogue'):
 # Nine-slice stretches only the center; original UI edges retain their proportions.
 im=Image.open(G/'gui/worlds'/world/f'{kind}.png').convert('RGBA'); sw,sh=im.size;b=24
 out=Image.new('RGBA',(int(w),int(h)))
 for ix,(a,z,da,dz) in enumerate([(0,b,0,b),(b,sw-b,b,int(w)-b),(sw-b,sw,int(w)-b,int(w))]):
  for iy,(c,d,dc,dd) in enumerate([(0,b,0,b),(b,sh-b,b,int(h)-b),(sh-b,sh,int(h)-b,int(h))]):
   out.paste(im.crop((a,c,z,d)).resize((dz-da,dd-dc)),(da,dc))
 path=TMP/f'panel_{len(P.slides)}_{x}_{y}.png';out.save(path);s.shapes.add_picture(str(path),u(x),u(y),u(w),u(h))
def scene(s,bgname,key,x,y,w,h,scale,cx):
 im=ImageOps.fit(Image.open(G/'images/backgrounds'/f'{bgname}.png').convert('RGBA'),(w,h))
 actor=Image.open(G/'images_normalized/olya'/f'{key}.png').convert('RGBA');actor=actor.resize((int(1600*scale),int(1600*scale)),Image.Resampling.LANCZOS)
 im.alpha_composite(actor,(int(cx-800*scale),0));path=TMP/f'scene_{len(P.slides)}_{x}.png';im.save(path);s.shapes.add_picture(str(path),u(x),u(y),u(w),u(h))

s=slide('Оля, с днем рождения! Эта игра — твое личное путешествие. Все начинается с одного совершенно обычного рабочего дня. А потом знакомая жизнь вдруг уступает место нескольким чужим мирам. В каждом из них ты остаешься главной героиней. И именно тебе решать, куда идти дальше.',N)
pic(s,ROOT/'art_sources/icon/game_icon.png',1040,100,820,820)
text(s,'ПОДАРОК ОЛЕ',100,110,850,70,34,GOLD,bold=True)
text(s,'В порядке\nперевода',95,260,1000,290,126,C,'Georgia')
text(s,'Один рабочий день.\nНесколько чужих миров.\nТвой выбор.',105,650,920,240,48,C)
rect(s,105,970,740,3,GOLD)

s=slide('Пока все очень узнаваемо: кабинет, бумаги и конец рабочего дня. Здесь к Оле обращаются «Ольга Игоревна», а у дел, кажется, нет привычки заканчиваться вовремя. Можно еще немного поработать. Но сначала хочется просто посидеть и ненадолго закрыть глаза. Что необычного может случиться за такую короткую паузу?')
bg(s,'office_evening');rect(s,0,0,1100,1080,N,87);sprite(s,'office/sleepy',1430)
text(s,'Все начинается\nна работе',95,100,1100,270,96,C,'Georgia')
panel(s,95,485,1000,270);text(s,'«Ольга Игоревна,\nвы еще здесь?»',140,540,900,170,60,B,'Georgia')
text(s,'«Я только посижу немного»',100,865,1100,100,48,C)

s=slide('А потом Оля открывает глаза. Только вместо кабинета вокруг солнечная Вистерия-Лейн. Она почему-то уже стоит, на ней другое платье, а в руках теплый пирог. Первую мысль лучше самой Оли не сформулируешь: «Так. Я же сидела». Как она здесь оказалась, пока неизвестно. Зато знакомиться с новым миром придется прямо сейчас.')
pic(s,G/'images/backgrounds/office_evening.png',0,0,780,1080);rect(s,0,0,780,1080,N,78)
pic(s,G/'images/backgrounds/wisteria_street.png',790,0,1130,1080);sprite(s,'housewives/pie',1450)
rect(s,780,0,10,1080,GOLD)
text(s,'«Так.\nЯ же сидела»',80,160,720,310,98,C,'Georgia')
text(s,'Вместо стула — солнце,\nплатье и пирог.',85,650,640,180,48,C)
rect(s,1035,940,805,110,N,94);text(s,'ВИСТЕРИЯ-ЛЕЙН',1090,970,700,65,34,C,bold=True)

s=slide('Впереди миры, которые легко узнать с первого взгляда. Сначала — уютные улицы и непростые разговоры «Отчаянных домохозяек». Затем — ритм Манхэттена из «Секса в большом городе». А потом — совсем другая логика Южного парка. Оля не наблюдает за ними со стороны: она оказывается внутри и отвечает за собственные поступки.')
title(s,'Знакомые миры…')
for x,bgname,key,label in [(80,'wisteria_street','housewives/gossip','Отчаянные\nдомохозяйки'),(680,'manhattan_street','manhattan/ironic','Секс в большом\nгороде'),(1280,'southpark_street','southpark/confused','Южный парк')]:
 scene(s,bgname,key,x,235,560,660,.62,280);rect(s,x,845,560,185,N);text(s,label,x+25,875,510,140,46,C,'Georgia')

s=slide('На этом путешествие не заканчивается. В Minecraft придется освоиться в квадратном мире и подумать об укрытии до ночи. В The Sims привычная жизнь получает свои игровые условности. А в Marvel масштаб происходящего снова меняется. У каждого мира своя атмосфера, свой вид и свои поводы удивиться. Интересно, где тебе захочется задержаться?')
title(s,'…и еще несколько неожиданных',size=80)
scene(s,'minecraft_clearing','minecraft/confused',80,240,1020,760,.72,420)
rect(s,80,865,1020,135,N,92);text(s,'Minecraft',125,895,900,90,70,C,'Georgia')
for y,bgn,key,label in [(240,'sims_home','sims/neutral','The Sims'),(650,'marvel_rooftop','marvel/power','Marvel')]:
 scene(s,bgn,key,1140,y,700,350,.42,520);rect(s,1140,y+230,700,120,N,90);text(s,label,1175,y+253,570,80,60,C,'Georgia')

s=slide('Посмотри, как вместе с миром меняется и сама Оля. В рисованной истории у нее одна пластика, в Minecraft — совсем другая геометрия. В The Sims появляется знакомый игровой образ, а Южный парк превращает ее в плоскую мультяшную героиню. При этом характер остается узнаваемым: она удивляется, сомневается, шутит и постепенно осваивается.')
title(s,'Мир меняется — и Оля тоже',size=83)
for cx,key,label in [(265,'office/skeptical','Рисованный мир'),(730,'minecraft/confused','Minecraft'),(1190,'sims/neutral','The Sims'),(1655,'southpark/neutral','Южный парк')]:
 sprite(s,key,cx,.83,155)
rect(s,0,955,1920,125,B)
for x,label in [(55,'Рисованный мир'),(565,'Minecraft'),(1040,'The Sims'),(1480,'Южный парк')]:text(s,label,x,993,425,70,37,C,bold=True)

s=slide('Здесь можно выбирать. Например, это настоящий момент из Minecraft: вечер приближается, и Оле нужен план. Собрать дерево и построить свое укрытие? Или успеть к деревне до темноты? Решения меняют то, как развиваются события. А еще в каждом мире можно остаться. Продолжать путешествие или остановиться — тоже твой выбор.')
bg(s,'minecraft_clearing');rect(s,0,0,1920,200,N,85);sprite(s,'minecraft/confused',450,y=145)
title(s,'Здесь можно выбирать',C,88)
panel(s,850,265,1000,285,'minecraft');text(s,'Оля',890,215,800,60,39,C,bold=True)
text(s,'Видишь, человек. Вернее, овца.\nУ нее есть план на вечер.\nМне тоже нужен.',900,310,895,215,47,'202020')
for y,t in [(610,'Собрать дерево и построить\nсвое укрытие'),(810,'Идти к деревне до темноты')]:
 panel(s,850,y,1000,155,'minecraft','choice_idle');text(s,t,900,y+33,895,110,43,'202020')

s=slide('Оля, куда отправимся? Пусть этот маленький подарок станет началом хорошего вечера. Здесь можно узнавать любимые миры, смеяться над неожиданностями и выбирать свой путь без спешки. С днем рождения! Желаю тебе побольше радости, интересных встреч и хороших историй впереди. А свою историю в этой игре пора начать прямо сейчас.',N)
bg(s,'office_day');rect(s,0,0,1920,1080,N,88);sprite(s,'office/happy',1460)
text(s,'Оля, куда\nотправимся?',95,190,1200,310,120,C,'Georgia')
text(s,'С днем рождения!\nПусть впереди будет много\nхороших историй.',105,605,1050,225,48,C)
panel(s,100,875,850,135);text(s,'Пора запускать игру',150,914,760,85,52,B,'Georgia')

P.core_properties.title='В порядке перевода — подарок Оле'
P.core_properties.subject='Демонстрация визуальной новеллы перед запуском'
P.core_properties.author='Для Оли'
P.save(OUT/'olya_birthday_presentation.pptx')
(TMP/'text_boxes.json').write_text(json.dumps(boxes,ensure_ascii=False,indent=2))
notes='\n\n'.join(f'Слайд {i+1}\n{s.notes_slide.notes_text_frame.text}' for i,s in enumerate(P.slides))
(OUT/'olya_birthday_speaker_notes.txt').write_text(notes,encoding='utf-8')
print('Created 8 slides;',len(notes.split()),'words in notes')
