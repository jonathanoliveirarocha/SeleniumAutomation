from selenium import webdriver
import time

navegador = webdriver.Chrome()

navegador.get("https://www.lncc.br/~borges/php/testar.html")
time.sleep(1)
navegador.find_element("xpath", '/html/body/center/form/textarea').clear()
time.sleep(1)
navegador.find_element("xpath", '/html/body/center/form/textarea').click()
time.sleep(1)
navegador.find_element("xpath", '/html/body/center/form/textarea').send_keys('<html><body><style>/* Animation from: https://pt.stackoverflow.com/questions/290086/efeito-escrita-dinamica-de-texto */html{height: 100%;overflow:hidden;}body{height: 100%;width: 100%;color: #fff;font-family: "Anonymous Pro", monospace;background-color: black;display: flex;}.line{position: relative;width: 0px;margin: auto;border-right: 2px solid rgba(255, 255, 255, 0.75);font-size: 180%;text-align: center;white-space: nowrap;overflow: hidden;}.anim-typewriter{animation: typewriter 4s steps(26) 500ms infinite,blinkTextCursor 500ms steps(26) infinite normal;} @keyframes typewriter {0% {width: 0px;}10% {width: 0px;}25% {width:410px;}75% {width: 410px;}90% {width: 0px;}100% {width: 0px;}}@keyframes blinkTextCursor {from {border-right-color: rgba(255, 255, 255, 0.75);}to {border-right-color: transparent;}}</style><p class="line anim-typewriter">Hello, thanks for viewing!</p></body></html>')
time.sleep(1)
navegador.find_element("xpath", '/html/body/center/form/input').click()
time.sleep(30)