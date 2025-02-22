import telebot

bot = telebot.TeleBot('8046673648:AAFxJOpXxLwkpi03o9qbcQY5mtK2cu4W6WA')

@bot.message_handler(commands=['vivih'])
def vivih(message):
    bot.send_message(message.chat.id, '*ВЫВИХ*\n'
                                      'Вывих – это смещение суставных концов костей, частично или полностью нарушающее их взаимное соприкосновение.\n'
                                      'ПРИЗНАКИ:\n'
                                      'появление интенсивной боли в области пораженного сустава;нарушение функции конечности, проявляющееся в невозможности производить активные движения;вынужденное положение конечности и деформация формы сустава;смещение суставной головки с запустеванием суставной капсулы и пружинящая фиксация конечности при ее ненормальном положении.\n'
                                      'Травматические вывихи суставов требуют немедленного оказания первой помощи. Своевременно вправленный вывих, при правильном последующем лечении, приведет к полному восстановлению нарушенной функции конечности.\n'
                                      '*ПЕРВАЯ ПОМОЩЬ* должна состоять, как правило, в фиксации поврежденной конечности, даче обезболивающего препарата и направлении пострадавшего в лечебное учреждение. Фиксация конечности осуществляется повязкой или подвешиванием ее на косынке. При вывихах суставов нижней конечности пострадавший должен быть доставлен в лечебное учреждение в лежачем положении (на носилках), с подкладыванием под конечность подушек, ее фиксацией и даче пострадавшему обезболивающего средства. При оказании первой помощи в неясных случаях, когда не представилось возможным отличить вывих от перелома, с пострадавшим следует поступать так, будто у него явный перелом костей.', parse_mode='Markdown')

@bot.message_handler(commands=['obmorok'])
def obmorok(message):
    bot.send_message(message.chat.id, '*ОБМОРОК*\nОБМОРОК – внезапная кратковременная потеря сознания, сопровождающаяся ослаблением деятельности сердца и дыхания. Возникает при быстро развивающемся малокровии головного мозга и продолжается от нескольких секунд до 5-10 минут и более.\nПРИЗНАКИ. Обморок выражается во внезапно наступающей дурноте, головокружении, слабости и потере сознания. Обморок сопровождается побледнением и похолоданием кожных покровов. Дыхание замедленное, поверхностное, слабый и редкий пульс (до 40-50 ударов в минуту).\n*ПЕРВАЯ ПОМОЩЬ*.\nПрежде всего, необходимо пострадавшего уложить на спину так, чтобы голова была несколько опущена, а ноги приподняты. Для облегчения дыхания освободить шею и грудь от стесняющей одежды. Тепло укройте пострадавшего, положите грелку к его ногам. Натрите нашатырным спиртом виски больного и поднесите к носу ватку, смоченную нашатырем, а лицо обрызгайте холодной водой. При затянувшемся обмороке показано искусственное дыхание. После прихода в сознание дайте ему горячий кофе.', parse_mode='Markdown')

@bot.message_handler(commands=['site'])
def site(message):
    bot.send_message(message.chat.id, '*https://www.bsmp.by/press-tsentr/polezno-znat/pervaya-pomoshch-chto-delat/pravila-okazaniya-pervoj-meditsinskoj-pomoshchi*', parse_mode='Markdown')


bot.infinity_polling()

