import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
str1 = """
日照香炉生紫烟，
遥看瀑布挂前川。
飞流直下三千尺，
疑是银河落九天。
"""
speaker.Speak(str1)
for i in range(1, 6):
    speaker.Speak("第" + str(i) + "次")
