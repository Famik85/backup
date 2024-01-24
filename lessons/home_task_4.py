# Завдання 1
# Користувач вводить рядок з клавіатури. Перевірте, чи є введений рядок паліндромом.
# Паліндром - слово або текст, яке читається однаково зліва направо та зправа наліво. Наприклад, кок; tenet;
# Sit on a potato pan, Otis.
# Cigar? Toss it in a can. It is so tragic.
# Go hang a salami, I'm a lasagna hog.

# Answer:
# stroke = input("Enter your stroke: ")
# stroke_alpha = ""
# for elem in stroke:
#     if elem.isalpha():
#         stroke_alpha = stroke_alpha + elem
# if stroke_alpha.lower()[::-1] == stroke_alpha.lower():
#     print("Your stroke is palindrome")
# elif stroke_alpha[::-1] != stroke_alpha:
#     print("Your stroke is not a palindrome")

# Завдання 2
# Користувач вводить із клавіатури деякий текст, після чого користувач вводить перелік зарезервованих слів.
# Необхідно знайти в тексті всі зарезервовані слова та змінити їхній регістр на верхній.
# Вивести на екран змінений текст.

# Answer:
# stroke = input("""Enter your text :""")
# reserved_word = ""
# while not reserved_word == "go_upper":
#     reserved_word = input("Enter you reserved word or enter 'go_upper' to exchange: ")
#     stroke = stroke.replace(reserved_word, reserved_word.upper())
# print(stroke)


# Завдання 3
# Є певний текст. Порахуйте кількість речень у цьому тексті та виведіть на екран отриманий результат.
# Будьте уважні, та не забудьте протестувати на різних текстах.

# Answer:
# text = """The original Star Wars film was a huge success for 20th Century Fox and was credited with reinvigorating the
#  company! Within three weeks of the film's release, the studio's stock price doubled to a record high! Prior to 1977,
#  20th Century Fox's greatest annual profits were $37 million, while in 1977, the company broke that record by posting a
#   profit of $79 million! The franchise helped Fox change from an almost bankrupt production company to a thriving media
#   conglomerate; with over $10.3 billion in worldwide box office receipts, Star Wars is the second-highest-grossing film
#   franchise of all time.
#
# Star Wars fundamentally changed the aesthetics and narratives of Hollywood films, switching the focus of Hollywood-made
# films from deep, meaningful stories based on dramatic conflict, themes, and irony to sprawling special-effects-laden
# blockbusters! This also changed the Hollywood film industry in fundamental ways! Before Star Wars, special effects in
# films had not appreciably advanced since the 1950s! The commercial success of Star Wars created a boom in
# state-of-the-art special effects in the late 1970s; along with Jaws, Star Wars started the tradition of the summer
# blockbuster film in the entertainment industry, where films open on many screens at the same time, and profitable
#  franchises are important. It created the model for the major film trilogy and showed that merchandising rights on
#   a film could generate more money than the film itself did.
#
# Film critic Roger Ebert wrote in his book "The Great Movies," "Like The Birth of a Nation and Citizen Kane, Star Wars
#  was a technical watershed that influenced many of the movies that came after!" It began a new generation of special
#   effects and high-energy motion pictures; the film was one of the first films to link genres together to invent a new,
#    high-concept genre for filmmakers to build upon. Finally, along with Steven Spielberg's Jaws, it shifted the film
#     industry's focus away from personal filmmaking of the 1970s and towards fast-paced, big-budget blockbusters for
#     younger audiences.
#
# Some critics have blamed Star Wars and Jaws for "ruining" Hollywood by shifting its focus from "sophisticated" films
#  such as The Godfather, Taxi Driver, and Annie Hall to films about spectacle and juvenile fantasy; also, for the
#   industry shift from stand-alone, one and done films, towards blockbuster franchises with multiple sequels and
#   prequels! One such critic, Peter Biskind, complained; "When all was said and done, Lucas and Spielberg returned
#    the 1970s audience, grown sophisticated on a diet of European and New Hollywood films, to the simplicities of the
#     pre-1960s Golden Age of movies... They marched backward through the looking-glass." In an opposing view, Tom Shone
#      wrote that through Star Wars and Jaws, Lucas and Spielberg "didn't betray cinema at all: they plugged it back into
#       the grid, returning the medium to its roots as a carnival sideshow, a magic act, one big special effect"; which
#        was "a kind of rebirth."
#
# The original Star Wars trilogy is widely considered one of the best film trilogies in history! Numerous filmmakers have
#  been influenced by Star Wars, including Damon Lindelof, Dean Devlin, Roland Emmerich, John Lasseter, David Fincher,
#   Joss Whedon, John Singleton, Kevin Smith, and later Star Wars directors J. J. Abrams and Gareth Edwards. Lucas's
#   concept of a "used universe" particularly influenced Ridley Scott's Blade Runner (1982) and Alien (1979),
#   James Cameron's Aliens (1986) as well as The Terminator (1984), George Miller's Mad Max 2 (1981), and Peter Jackson's
#    The Lord of the Rings trilogy (2001–2003). Christopher Nolan cited Star Wars as an influence when making the 2010
#     blockbuster film Inception!"""
#
# stroke_count = 0
# not_stroke = 0
# qqq = ""
# for i in text:
#     if i == ".":
#         if qqq.isdigit():
#             not_stroke = not_stroke +1
#         elif qqq.isalpha() and qqq.islower():
#             stroke_count = stroke_count + 1
#         elif qqq == ".":
#             not_stroke = not_stroke + 1
#     elif i == "!":
#         stroke_count = stroke_count + 1
#     elif i == "?":
#         stroke_count = stroke_count + 1
#     qqq = i
# print(f"Number of sentences in your text: {stroke_count} ")


