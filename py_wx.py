from wxpy import Bot


def loginAndSend(filename):
    bot = Bot()
    myself = bot.self
    username = myself.user_name
    bot.file_helper.send('Welcome ' + username)
    bot.file_helper.send_file(filename)
    # bot.logout()


if __name__ == '__main__':
    loginAndSend('d:/test.docx')