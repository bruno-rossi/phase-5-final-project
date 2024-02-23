from app import app
from models import db, User, Course, UserCourse, Lesson, Language, UserLesson

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        UserLesson.query.delete()
        UserCourse.query.delete()
        Language.query.delete()
        User.query.delete()
        Course.query.delete()
        Lesson.query.delete()

        db.session.commit()

        print("Seeding...")

        print("Seeding users...")

        user1 = User(email="brunogabrielrossi@gmail.com", name="")
        user1.password_hash = "test"

        user2 = User(email="andrew@test.com", name="")
        user2.password_hash = "test"

        user3 = User(email="katie@test.com", name="")
        user3.password_hash = "test"

        users = [
            user1,
            user2,
            user3
        ]

        db.session.add_all(users)
        db.session.commit()

        print("Seeding languages...")
        portuguese = Language(
            language_name="Portuguese (Brazil)",
            language_code="pt-BR"
        )
        greek = Language(
            language_name="Greek",
            language_code="el-GR"
        )
        english = Language(
            language_name="English (US)",
            language_code="en-US"
        )
        french = Language(
            language_name="French (France)",
            language_code="fr-FR"
        )

        languages = [ portuguese, greek, english, french]
        db.session.add_all(languages)
        db.session.commit()

        print("Seeding courses...")
        course1_portuguese = Course(
            title="Brazilian Music",
            language_id=1
        )

        course1_greek = Course(
            title="Greek Islands",
            language_id="2"
        )

        course1_english = Course(
            title="2000s Pop Music",
            language_id="3"
        )

        courses = [ course1_portuguese, course1_greek, course1_english]
        db.session.add_all(courses)
        db.session.commit()

        print("Seeding lessons...")
        lesson1 = Lesson(
            language_id="1",
            course_id="1",
            title="Bossa Nova",
            prev_lesson="",
            next_lesson="2",
            lesson_type="reading",
            content="""A Bossa Nova é um gênero musical brasileiro que surgiu no final dos anos 1950 e início dos anos 1960, principalmente no Rio de Janeiro. É conhecida por suas batidas suaves, melodia sofisticada e letras poéticas, incorporando influências do samba e do jazz. O gênero foi popularizado por músicos como João Gilberto, Tom Jobim e Vinicius de Moraes, cujas composições icônicas como "Garota de Ipanema" tornaram-se mundialmente famosas. A Bossa Nova não apenas revolucionou a música brasileira, mas também teve um impacto significativo na cena musical internacional, influenciando artistas ao redor do mundo.
            A atmosfera relaxante e a sensibilidade lírica da Bossa Nova refletem a atmosfera descontraída e ensolarada das praias do Rio de Janeiro, onde muitos dos músicos do gênero se reuniam para criar e se inspirar. As harmonias complexas e os arranjos inovadores caracterizam a sonoridade distintiva da Bossa Nova, que se tornou um símbolo da sofisticação e do charme brasileiro. Apesar de ter experimentado períodos de menor popularidade, a Bossa Nova continua a ser celebrada e reinterpretada até hoje, mantendo-se como uma parte essencial do rico patrimônio musical do Brasil."""
        )

        lesson2 = Lesson(
            language_id="1",
            course_id="1",
            title="Funk Carioca",
            prev_lesson="1",
            next_lesson="3",
            lesson_type="reading",
            content="""O Funk Carioca, também conhecido simplesmente como Funk, é um estilo musical originário das comunidades urbanas do Rio de Janeiro, Brasil. Surgido na década de 1970, o Funk Carioca é marcado por batidas pesadas, letras provocativas e uma mistura de influências que incluem o Miami Bass, o hip-hop e o funk norte-americano. Suas origens estão intimamente ligadas às festas de rua e bailes funk das favelas cariocas, onde os DJs locais tocavam músicas em vinil, improvisando com samples e criando uma atmosfera de celebração e dança. Ao longo dos anos, o Funk Carioca evoluiu e diversificou-se, abraçando diferentes subgêneros e influências musicais, enquanto mantinha sua essência pulsante e vibrante.
            Apesar de sua popularidade crescente, o Funk Carioca também tem sido objeto de controvérsia devido às suas letras explícitas e temas controversos, muitas vezes retratando a realidade das comunidades marginalizadas do Rio de Janeiro. No entanto, o gênero também tem sido reconhecido como uma forma de expressão cultural importante e uma voz para as comunidades menos privilegiadas, refletindo suas lutas, aspirações e identidades. Com sua batida inconfundível e letras que misturam crítica social e diversão, o Funk Carioca continua a ser uma força influente na cena musical brasileira e uma parte integral da cultura urbana do Rio de Janeiro."""
        )

        lesson3 = Lesson(
            language_id="1",
            course_id="1",
            title="MPB -  Música Popular Brasileira",
            prev_lesson="2",
            next_lesson="",
            lesson_type="reading",
            content="""A Música Popular Brasileira, conhecida como MPB, é um gênero musical que reflete a riqueza e a diversidade cultural do Brasil. Surgida na década de 1960, a MPB é uma fusão de diversos estilos musicais, como o samba, o baião, a bossa nova, o rock, entre outros, combinados com letras poéticas que frequentemente abordam temas sociais, políticos e culturais. Artistas como Caetano Veloso, Gilberto Gil, Chico Buarque, Elis Regina e Milton Nascimento são algumas das figuras emblemáticas que contribuíram para a consolidação e popularização da MPB, tanto no Brasil quanto no exterior.

            A MPB desfrutou de várias fases ao longo das décadas, passando por momentos de repressão durante a ditadura militar brasileira, quando suas letras politizadas eram censuradas, até períodos de grande reconhecimento internacional, quando artistas brasileiros conquistaram palcos ao redor do mundo. Atualmente, a MPB continua a ser uma força vital na cena musical brasileira, com uma geração mais jovem de artistas reinterpretando e renovando o gênero, mantendo sua relevância e sua capacidade de emocionar e inspirar pessoas de todas as idades e origens."""
        )

        lesson4 = Lesson(
            language_id="2",
            course_id="2",
            title="Mykonos",
            prev_lesson="",
            next_lesson="5",
            lesson_type="reading",
            content="""Η Μύκονος είναι ένα από τα πιο δημοφιλή νησιά της Ελλάδας, γνωστό για τη ζωντάνια της νυχτερινής ζωής της και τις εντυπωσιακές παραλίες της. Το νησί είναι προσελκυστικό προορισμός για τους επισκέπτες που αναζητούν διασκέδαση, με μια πληθώρα μπαρ, εστιατορίων και νυχτερινών κέντρων που προσφέρουν μοναδικές εμπειρίες. Ωστόσο, η Μύκονος δεν περιορίζεται μόνο στη νυχτερινή ζωή, αλλά προσφέρει επίσης όμορφα χωριά με παραδοσιακή αρχιτεκτονική και εντυπωσιακά τοπία για τους λάτρεις της φύσης."""
        )

        lesson5 = Lesson(
            language_id="2",
            course_id="2",
            title="Crete",
            prev_lesson="4",
            next_lesson="6",
            lesson_type="reading",
            content="""Η Κρήτη, η μεγαλύτερη νήσος της Ελλάδας, είναι ένας πολυσύχναστος προορισμός με πλούσια ιστορία και πολιτισμό. Με πανέμορφες παραλίες, αρχαιολογικούς χώρους και παραδοσιακά χωριά, η Κρήτη προσελκύει εκατομμύρια τουρίστες κάθε χρόνο. Οι επισκέπτες μπορούν να απολαύσουν τη γαστρονομία του νησιού, που περιλαμβάνει τοπικά προϊόντα και παραδοσιακές συνταγές, καθώς και να εξερευνήσουν τα μοναδικά τοπία και τα φυσικά αξιοθέατα της Κρήτης."""
        )

        lesson6 = Lesson(
            language_id="2",
            course_id="2",
            title="Santorini",
            prev_lesson="5",
            next_lesson="",
            lesson_type="reading",
            content="""Η Σαντορίνη είναι γνωστή για τα εντυπωσιακά της ηλιοβασιλέματα, τα λευκά χωριά της με τις μπλε οροφές και τις καταπράσινες κρατήσεις των καλντερών. Το νησί προσφέρει μια ρομαντική ατμόσφαιρα και είναι ιδανικό για ζευγάρια που αναζητούν μια αξέχαστη εμπειρία. Οι επισκέπτες μπορούν επίσης να απολαύσουν την τοπική κουζίνα και τον κρασί της Σαντορίνης, καθώς και να εξερευνήσουν τις ιστορικές πόλεις και τους αρχαιολογικούς χώρους του νησιού."""
        )

        lesson7 = Lesson(
            language_id="3",
            course_id="3",
            title="Emergence of Pop Divas",
            prev_lesson="",
            next_lesson="7",
            lesson_type="reading",
            content="""The 2000s witnessed the rise of iconic pop divas who dominated the music scene with their powerful vocals and captivating performances. Artists like Britney Spears, Christina Aguilera, and Beyoncé became household names, shaping the sound and style of pop music during this era. Britney Spears, often referred to as the "Princess of Pop," gained immense popularity with hits like "Oops!... I Did It Again" and "Toxic," while Christina Aguilera showcased her vocal prowess with songs like "Beautiful" and "Genie in a Bottle." Beyoncé, who began her career as part of Destiny's Child before embarking on a solo journey, solidified her status as a global superstar with albums like "Dangerously in Love" and "B'Day," paving the way for her later success as a multi-talented artist and businesswoman.
            
            Additionally, the 2000s saw the emergence of teen pop sensations like Justin Timberlake and the boy bands *NSYNC and Backstreet Boys, who gained massive fan followings with their catchy tunes and synchronized dance routines. Justin Timberlake, known for his smooth vocals and charismatic stage presence, transitioned from his boy band days in *NSYNC to a successful solo career with albums like "Justified" and "FutureSex/LoveSounds." The boy bands *NSYNC and Backstreet Boys dominated the charts with hits like "*NSYNC's "Bye Bye Bye" and Backstreet Boys' "I Want It That Way," captivating audiences with their infectious pop melodies and youthful energy. Collectively, these pop acts defined the sound of the 2000s and left a lasting impact on the music industry and pop culture as a whole."""
        )

        lesson8 = Lesson(
            language_id="3",
            course_id="3",
            title="Influence of Reality TV Shows on Pop Music",
            prev_lesson="7",
            next_lesson="",
            lesson_type="reading",
            content="""The 2000s marked the era of reality TV shows that not only entertained audiences but also served as a platform for discovering new talent and shaping the landscape of pop music. Shows like "American Idol" and "The X Factor" became cultural phenomena, propelling aspiring singers to stardom and introducing them to a global audience. Artists such as Kelly Clarkson, Carrie Underwood, and Jennifer Hudson rose to prominence after winning "American Idol," showcasing their vocal abilities and captivating audiences with their performances. These reality TV competitions not only provided a platform for undiscovered talent but also played a significant role in shaping popular music trends and influencing the music industry.
            Furthermore, reality TV shows like "Making the Band" and "The Pussycat Dolls Present: The Search for the Next Doll" showcased the behind-the-scenes process of forming musical groups, offering viewers a glimpse into the challenges and triumphs of aspiring artists. "Making the Band" famously chronicled the creation of musical acts like O-Town and Danity Kane, while "The Pussycat Dolls Present" aimed to assemble the next member of the popular girl group. These shows not only entertained audiences but also highlighted the rigorous training and dedication required to succeed in the competitive world of pop music. Overall, reality TV shows played a significant role in shaping the pop music landscape of the 2000s, contributing to the discovery of new talent and the creation of chart-topping hits."""
        )

        lessons = [ lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8]
        db.session.add_all(lessons)
        db.session.commit()

        # print("Adding courses to users...")

        print("Done seeding!")