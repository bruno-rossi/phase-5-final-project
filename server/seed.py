from app import app
from models import db, User, Course, UserCourse, Lesson, Language, UserLesson, Topic, UserTopic, Question, UserQuestion

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        UserLesson.query.delete()
        UserCourse.query.delete()
        UserTopic.query.delete()
        UserQuestion.query.delete()
        Language.query.delete()
        Topic.query.delete()
        User.query.delete()
        Course.query.delete()
        Lesson.query.delete()
        Question.query.delete()

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

        print("Seeding topics...")
        music = Topic(
            topic_name="Music",
            topic_description="Lessons about music and history of musical arts."
        )

        geography = Topic(
            topic_name="Geography",
            topic_description="Courses and lessons about the world."
        )

        mythology = Topic(
            topic_name="Mythology",
            topic_description="Learn about myths and traditional stories."
        )

        cuisine = Topic(
            topic_name="Cuisine",
            topic_description="Learn about food and culinary stories."
        )

        topics = [ music, geography, mythology, cuisine ]
        db.session.add_all(topics)
        db.session.commit()

        print("Seeding courses...")
        course1_portuguese = Course(
            title="Brazilian Music",
            description="Learn about different genres in Brazilian Music, the history and culture behind them.",
            image="https://langlittravel.files.wordpress.com/2020/09/brazil-carnival-character-dance-samba-set-vector-23364787.jpg",
            language_id="1",
            topic_id="1"
        )

        course1_greek = Course(
            title="Greek Islands",
            description="Explore the history and geography of the Greek Islands.",
            image="https://img.freepik.com/free-vector/hand-drawn-mykonos-illustration_52683-85201.jpg",
            language_id="2",
            topic_id="2"
        )

        course1_english = Course(
            title="2000s Pop Music",
            description="Learn about the pop music phenomenon post Y2K.",
            image="https://upload.wikimedia.org/wikipedia/commons/f/f8/Pop_Music_Barnstar.png",
            language_id="3",
            topic_id="1"
        )

        course2_greek = Course(
            title="Greek Mythology",
            description="Discover the myths and stories from Greek Mythology while practicing the Genitive Case.",
            image="https://t4.ftcdn.net/jpg/05/65/17/01/360_F_565170181_BlcgmJNx773mOxf6TtiXYHlMrdBeN9Hr.jpg",
            language_id="2",
            topic_id="3"
        )

        course3_greek = Course(
            title="Gods versus Titans",
            description="Learn about the Greek Myth of Titanomachy (the war between titans and gods) and practice the Aorist Tense.",
            image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Cornelis_Cornelisz._van_Haarlem_-_The_Fall_of_the_Titans_-_Google_Art_Project.jpg/640px-Cornelis_Cornelisz._van_Haarlem_-_The_Fall_of_the_Titans_-_Google_Art_Project.jpg",
            language_id="2",
            topic_id="3"
        )

        course4_greek = Course(
            title="The magic of Greek cuisine",
            description="Learn about Greek cuisine and its most famous dishes while practicing noun declensions.",
            image="https://media.scoolinary.app/images/2022/05/253806_custom_site_themes_id_HEZyicURRLi6tAGabrvp_196-Banner-Landing-Curso-Scoolinary-2.png",
            language_id="2",
            topic_id="4"
        )
        
        course5_greek = Course(
            title="Traditional Greek desserts",
            description="Learn about Greek sweets while practicing noun declensions.",
            image="https://www.greekboston.com/wp-content/uploads/2020/03/baklava-scaled.jpg",
            language_id="2",
            topic_id="4"
        )

        course2_portuguese = Course(
            title="Introduction to Brazilian Cuisine",
            description="An overview of the diverse culinary traditions across Brazil's regions. Explore iconic dishes such as feijoada, coxinha, acarajé, and moqueca.",
            image="https://gatewaytobrazil.com/wp-content/uploads/2021/03/Brazilian-food-1-scaled-e1615435790537-768x512.jpeg",
            language_id="1",
            topic_id="4"
        )
        
        course3_portuguese = Course(
            title="Tropical fruits of Brazil",
            description="Learn about tropical fruits found in Brazil.",
            image="https://tudoela.com/wp-content/uploads/2018/12/Frutas-Tropicais-1.jpg",
            language_id="1",
            topic_id="4"
        )

        course4_portuguese = Course(
            title="Brazilian street food",
            description="Exploring popular street food snacks like pastel, tapioca, and pão de queijo.",
            image="https://foodmagazine.com.br/imagens/noticias/butatan_food_park.jpg",
            language_id="1",
            topic_id="4"
        )

        course5_portuguese = Course(
            title="Cuisine in the Brazilian rainforest region",
            description="Delve into the unique culinary traditions of the Amazon",
            image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyZo8zdC06GCSB4ZknMEtU11WaCWuM6titSA&usqp=CAU",
            language_id="1",
            topic_id="4"
        )

        course7_portuguese = Course(
            title="The Brazilian churrasco",
            description="Understand the techniques, cuts of meat, and cultural significance of Brazilian barbecue.",
            image="https://legacy.travelnoire.com/wp-content/uploads/2021/09/575f5923d3a9a_gastronomia_churrascarias_fogo-de-chao.jpg",
            language_id="1",
            topic_id="4"
        )

        course8_portuguese = Course(
            title="Brazilian drinks and beverages",
            description="Explore traditional Brazilian drinks such as caipirinha, guaraná, and açaí smoothies. Learn about the origins of cachaça (Brazilian rum).",
            image="https://blog.amigofoods.com/wp-content/uploads/2019/06/caipirinhas-brazilian-cocktail.jpg",
            language_id="1",
            topic_id="4"
        )

        course9_portuguese = Course(
            title="Festa junina: typical festivals in Brazil",
            description="Explore traditional Brazilian drinks such as caipirinha, guaraná, and açaí smoothies. Learn about the origins of cachaça (Brazilian rum).",
            image="https://blog.amigofoods.com/wp-content/uploads/2022/02/festa-junina-brazil.jpg",
            language_id="1",
            topic_id="4"
        )

        course10_portuguese = Course(
            title="Melting pot: diverse cuisines in Brazil",
            description="Discussing the influences of indigenous, African, European, Asian, and immigrant cultures on Brazilian food.",
            image="https://tabularestaurante.com.br/wp-content/uploads/2020/08/Comidas-estrangeiras-consumidas-pelo-brasileiro-3-1024x576.jpg",
            language_id="1",
            topic_id="4"
        )

        courses = [ course1_portuguese, course1_greek, course2_greek, course3_greek, course1_english, course4_greek, course5_greek, course2_portuguese, course3_portuguese, course4_portuguese, course5_portuguese, course7_portuguese, course8_portuguese, course9_portuguese, course10_portuguese]
        db.session.add_all(courses)
        db.session.commit()

        print("Seeding lessons...")
        lesson1 = Lesson(
            language_id="1",
            topic_id="1",
            course_id="1",
            title="Bossa Nova",
            prev_lesson="",
            next_lesson="2",
            lesson_type="reading",
            content="""<p lang='pt-BR'>A Bossa Nova é um gênero musical brasileiro que surgiu no final dos anos 1950 e início dos anos 1960, principalmente no Rio de Janeiro. É conhecida por suas batidas suaves, melodia sofisticada e letras poéticas, incorporando influências do samba e do jazz. O gênero foi popularizado por músicos como João Gilberto, Tom Jobim e Vinicius de Moraes, cujas composições icônicas como "Garota de Ipanema" tornaram-se mundialmente famosas. A Bossa Nova não apenas revolucionou a música brasileira, mas também teve um impacto significativo na cena musical internacional, influenciando artistas ao redor do mundo.</p>
            <p lang='pt-BR'>A atmosfera relaxante e a sensibilidade lírica da Bossa Nova refletem a atmosfera descontraída e ensolarada das praias do Rio de Janeiro, onde muitos dos músicos do gênero se reuniam para criar e se inspirar. As harmonias complexas e os arranjos inovadores caracterizam a sonoridade distintiva da Bossa Nova, que se tornou um símbolo da sofisticação e do charme brasileiro. Apesar de ter experimentado períodos de menor popularidade, a Bossa Nova continua a ser celebrada e reinterpretada até hoje, mantendo-se como uma parte essencial do rico patrimônio musical do Brasil.</p>"""
        )

        lesson2 = Lesson(
            language_id="1",
            topic_id="1",
            course_id="1",
            title="Funk Carioca",
            prev_lesson="1",
            next_lesson="3",
            lesson_type="reading",
            content="""<p lang='pt-BR'>O Funk Carioca, também conhecido simplesmente como Funk, é um estilo musical originário das comunidades urbanas do Rio de Janeiro, Brasil. Surgido na década de 1970, o Funk Carioca é marcado por batidas pesadas, letras provocativas e uma mistura de influências que incluem o Miami Bass, o hip-hop e o funk norte-americano. Suas origens estão intimamente ligadas às festas de rua e bailes funk das favelas cariocas, onde os DJs locais tocavam músicas em vinil, improvisando com samples e criando uma atmosfera de celebração e dança. Ao longo dos anos, o Funk Carioca evoluiu e diversificou-se, abraçando diferentes subgêneros e influências musicais, enquanto mantinha sua essência pulsante e vibrante.</p>
            <p lang='pt-BR'>Apesar de sua popularidade crescente, o Funk Carioca também tem sido objeto de controvérsia devido às suas letras explícitas e temas controversos, muitas vezes retratando a realidade das comunidades marginalizadas do Rio de Janeiro. No entanto, o gênero também tem sido reconhecido como uma forma de expressão cultural importante e uma voz para as comunidades menos privilegiadas, refletindo suas lutas, aspirações e identidades. Com sua batida inconfundível e letras que misturam crítica social e diversão, o Funk Carioca continua a ser uma força influente na cena musical brasileira e uma parte integral da cultura urbana do Rio de Janeiro.</p>"""
        )

        lesson3 = Lesson(
            language_id="1",
            topic_id="1",
            course_id="1",
            title="MPB -  Música Popular Brasileira",
            prev_lesson="2",
            next_lesson="",
            lesson_type="reading",
            content="""<p lang='pt-BR'>A Música Popular Brasileira, conhecida como MPB, é um gênero musical que reflete a riqueza e a diversidade cultural do Brasil. Surgida na década de 1960, a MPB é uma fusão de diversos estilos musicais, como o samba, o baião, a bossa nova, o rock, entre outros, combinados com letras poéticas que frequentemente abordam temas sociais, políticos e culturais. Artistas como Caetano Veloso, Gilberto Gil, Chico Buarque, Elis Regina e Milton Nascimento são algumas das figuras emblemáticas que contribuíram para a consolidação e popularização da MPB, tanto no Brasil quanto no exterior.</p>
            <p lang='pt-BR'>A MPB desfrutou de várias fases ao longo das décadas, passando por momentos de repressão durante a ditadura militar brasileira, quando suas letras politizadas eram censuradas, até períodos de grande reconhecimento internacional, quando artistas brasileiros conquistaram palcos ao redor do mundo. Atualmente, a MPB continua a ser uma força vital na cena musical brasileira, com uma geração mais jovem de artistas reinterpretando e renovando o gênero, mantendo sua relevância e sua capacidade de emocionar e inspirar pessoas de todas as idades e origens.</p>"""
        )

        lesson4 = Lesson(
            language_id="2",
            topic_id="2",
            course_id="2",
            title="Mykonos",
            prev_lesson="",
            next_lesson="5",
            lesson_type="reading",
            content="""<p lang='el-GR'>Η Μύκονος είναι ένα από τα πιο δημοφιλή νησιά της Ελλάδας, γνωστό για τη ζωντάνια της νυχτερινής ζωής της και τις εντυπωσιακές παραλίες της. Το νησί είναι προσελκυστικό προορισμός για τους επισκέπτες που αναζητούν διασκέδαση, με μια πληθώρα μπαρ, εστιατορίων και νυχτερινών κέντρων που προσφέρουν μοναδικές εμπειρίες. Ωστόσο, η Μύκονος δεν περιορίζεται μόνο στη νυχτερινή ζωή, αλλά προσφέρει επίσης όμορφα χωριά με παραδοσιακή αρχιτεκτονική και εντυπωσιακά τοπία για τους λάτρεις της φύσης.</p>"""
        )

        lesson5 = Lesson(
            language_id="2",
            topic_id="2",
            course_id="2",
            title="Crete",
            prev_lesson="4",
            next_lesson="6",
            lesson_type="reading",
            content="""<p lang='el-GR'>Η Κρήτη, η μεγαλύτερη νήσος της Ελλάδας, είναι ένας πολυσύχναστος προορισμός με πλούσια ιστορία και πολιτισμό. Με πανέμορφες παραλίες, αρχαιολογικούς χώρους και παραδοσιακά χωριά, η Κρήτη προσελκύει εκατομμύρια τουρίστες κάθε χρόνο. Οι επισκέπτες μπορούν να απολαύσουν τη γαστρονομία του νησιού, που περιλαμβάνει τοπικά προϊόντα και παραδοσιακές συνταγές, καθώς και να εξερευνήσουν τα μοναδικά τοπία και τα φυσικά αξιοθέατα της Κρήτης.</p>"""
        )

        lesson6 = Lesson(
            language_id="2",
            topic_id="2",
            course_id="2",
            title="Santorini",
            prev_lesson="5",
            next_lesson="",
            lesson_type="reading",
            content="""<p lang='el-GR'>Η Σαντορίνη είναι γνωστή για τα εντυπωσιακά της ηλιοβασιλέματα, τα λευκά χωριά της με τις μπλε οροφές και τις καταπράσινες κρατήσεις των καλντερών. Το νησί προσφέρει μια ρομαντική ατμόσφαιρα και είναι ιδανικό για ζευγάρια που αναζητούν μια αξέχαστη εμπειρία. Οι επισκέπτες μπορούν επίσης να απολαύσουν την τοπική κουζίνα και τον κρασί της Σαντορίνης, καθώς και να εξερευνήσουν τις ιστορικές πόλεις και τους αρχαιολογικούς χώρους του νησιού.</p>"""
        )

        lesson9 = Lesson(
            language_id="2",
            topic_id="3",
            course_id="3",
            title="The birth of Zeus",
            prev_lesson="",
            next_lesson="10",
            lesson_type="reading",
            content="<p lang='el-GR'>Μια φορά, στην αρχαία Ελλάδα, ζούσε ο βασιλιάς Κρόνος, ο οποίος φοβούμενος την προφητεία που έλεγε ότι θα ανατραπεί από τον γιο του, κατάπινε τα παιδιά του αμέσως μόλις γεννιούνταν. Όταν όμως η σύζυγός του, Ρέα, γέννησε τον Δία, αποφάσισε να προστατέψει τον γιο του. Έτσι, αντί για να τον καταπιεί, έφαγε έναν λίθο, και ο Δίας απέφυγε το μοιραίο πεπρωμένο. Όταν μεγάλωσε, ο Δίας επαναστάτησε ενάντια στον πατέρα του και τους Τιτάνες, και τελικά κατάφερε να γίνει ο άρχοντας του ουρανού.</p>"
        )

        lesson10 = Lesson(
            language_id="2",
            topic_id="3",
            course_id="3",
            title="Orion and Arthemis",
            prev_lesson="9",
            next_lesson="11",
            lesson_type="reading",
            content="<p lang='el-GR'>Σε μια άλλη ιστορία, η Αρτέμις, η θεά του κυνηγιού και των δασών, ήταν γνωστή για την αγάπη της προς τη φύση και τα άγρια ζώα. Μαζί με τον αδερφό της, τον Απόλλωνα, περιφρόνησαν τον Ορίωνα, έναν κυνηγό που τολμούσε να τους προσεγγίσει. Ο Ορίωνας, παρά τις προειδοποιήσεις τους, προσπάθησε να τους αποσπάσει από το έδαφος, αλλά η θεά Αρτέμις, προστάτης των νεαρών κοριτσιών, τον μεταμόρφωσε σε αστέρι, που ακόμη και σήμερα λάμπει στον ουρανό με τη λαμπρή του λάμψη.</p>"
        )

        lesson11 = Lesson(
            language_id="2",
            topic_id="3",
            course_id="3",
            title="Paris and Helen",
            prev_lesson="10",
            next_lesson="",
            lesson_type="reading",
            content="<p lang='el-GR'>Τέλος, στην εποχή της Τρωάδας, ο Πάρις, γιος του βασιλιά Πρίαμου, ερωτεύτηκε την Ελένη, την ωραιότερη γυναίκα στον κόσμο, που ήταν παντρεμένη με τον βασιλιά της Σπάρτης. Καλείται να κρίνει ποια θεά είναι η ομορφότερη ανάμεσα στην Ήρα, την Αφροδίτη και την Αθηνά. Η Αφροδίτη, προσφέρνοντάς του την ωραιότερη γυναίκα, η Ελένη, ως αντάλλαγμα, κατέκτησε την καρδιά του και τον έπεισε να κλέψει την Ελένη και να ξεσπάσει ο θυμός των Έλληνων, που οδήγησε στον θρυλικό πόλεμο της Τροίας.</p>"
        )

        lesson12 = Lesson(
            language_id="2",
            topic_id="3",
            course_id="4",
            title="The Battle of the Gods",
            prev_lesson="",
            next_lesson="13",
            lesson_type="reading",
            content="<p lang='el-GR'>Η Μάχη των Θεών: Κατά τη διάρκεια της αρχαιότητας, οι θεοί του Ολύμπου και οι Τιτάνες έδωσαν μάχη για την κυριαρχία του κόσμου. Ο Κρόνος, ο ηγέτης των Τιτάνων, ορκίστηκε να εξουσιάσει τον κόσμο, εκδιώχνοντας τους θεούς του Ολύμπου. Κατά τη διάρκεια της μάχης, ο Δίας, ο ηγέτης των Ολυμπίων, οργισμένος για την προδοσία του πατέρα του, αντέστησε με θάρρος και δύναμη, εκμεταλλευόμενος τη βοήθεια των αδελφών του, του Ποσειδώνα και του Αίδη.</p><p lang='el-GR'>Η μάχη διήρκησε για αιώνες, με τις δυνάμεις να μάχονται σφοδρά για την επικράτηση. Τελικά, ο Δίας κατάφερε να ανατρέψει τον Κρόνο και τους Τιτάνες, κλείνοντάς τους στην Ταρταρούχτα, και επανακαθιέρωσε την τάξη στον Ολύμπο. Η μάχη αυτή έμεινε ως μια από τις μεγαλύτερες στιγμές στη μυθολογία, συμβολίζοντας τη νίκη του καλού επί του κακού και την επιστροφή της ειρήνης στον κόσμο.</p>"
        )

        lesson13 = Lesson(
            language_id="2",
            topic_id="3",
            course_id="4",
            title="The Titanic Traitor",
            prev_lesson="12",
            next_lesson="",
            lesson_type="reading",
            content="<p lang='el-GR'>Η Ανατροπή του Τιτανικού Προδότη: Κατά την περίοδο της αρχαιότητας, οι θεοί του Ολύμπου και οι Τιτάνες εναντιώθηκαν σε μια μάχη για την κυριαρχία του κόσμου. Ο Κρόνος, ο ηγέτης των Τιτάνων, προδόθηκε από τον Προμηθέα, τον οποίο είχε κερδίσει στο πλευρό του. Ο Προμηθέας, αναγνωρίζοντας την αδικία του Κρόνου και την κυριαρχία των θεών του Ολύμπου, ανέλαβε την πρωτοβουλία να ανατρέψει τον τυραννικό καθεστώς.</p><p lang='el-GR'>Με τη βοήθεια των θεών του Ολύμπου, ο Προμηθέας ξεσήκωσε επανάσταση ενάντια στους Τιτάνες και τον Κρόνο. Κατάφερε να κερδίσει την εμπιστοσύνη των άλλων θεών και να συγκεντρώσει δυνάμεις για τη μάχη. Μετά από μια μακρά και σκληρή μάχη, ο Προμηθέας και οι Ολύμπιοι θεοί κατάφεραν να ανατρέψουν τον Κρόνο και τους Τιτάνες, επαναφέροντας την τάξη και την ειρήνη στον κόσμο.</p>"
        )

        lesson7 = Lesson(
            language_id="3",
            topic_id="1",
            course_id="5",
            title="Emergence of Pop Divas",
            prev_lesson="",
            next_lesson="7",
            lesson_type="reading",
            content="<p lang='en'>The 2000s witnessed the rise of iconic pop divas who dominated the music scene with their powerful vocals and captivating performances. Artists like Britney Spears, Christina Aguilera, and Beyoncé became household names, shaping the sound and style of pop music during this era. Britney Spears, often referred to as the \"Princess of Pop,\" gained immense popularity with hits like \"Oops!... I Did It Again\" and \"Toxic,\" while Christina Aguilera showcased her vocal prowess with songs like \"Beautiful\" and \"Genie in a Bottle.\" Beyoncé, who began her career as part of Destiny's Child before embarking on a solo journey, solidified her status as a global superstar with albums like \"Dangerously in Love\" and \"B\'Day,\" paving the way for her later success as a multi-talented artist and businesswoman.</p><p>Additionally, the 2000s saw the emergence of teen pop sensations like Justin Timberlake and the boy bands *NSYNC and Backstreet Boys, who gained massive fan followings with their catchy tunes and synchronized dance routines. Justin Timberlake, known for his smooth vocals and charismatic stage presence, transitioned from his boy band days in *NSYNC to a successful solo career with albums like \"Justified\" and \"FutureSex/LoveSounds.\" The boy bands *NSYNC and Backstreet Boys dominated the charts with hits like \"*NSYNC's \"Bye Bye Bye\" and Backstreet Boys' \"I Want It That Way,\" captivating audiences with their infectious pop melodies and youthful energy. Collectively, these pop acts defined the sound of the 2000s and left a lasting impact on the music industry and pop culture as a whole.</p>"
        )

        lesson8 = Lesson(
            language_id="3",
            topic_id="1",
            course_id="5",
            title="Influence of Reality TV Shows on Pop Music",
            prev_lesson="7",
            next_lesson="",
            lesson_type="reading",
            content="""<p lang='en'>The 2000s marked the era of reality TV shows that not only entertained audiences but also served as a platform for discovering new talent and shaping the landscape of pop music. Shows like "American Idol" and "The X Factor" became cultural phenomena, propelling aspiring singers to stardom and introducing them to a global audience. Artists such as Kelly Clarkson, Carrie Underwood, and Jennifer Hudson rose to prominence after winning "American Idol," showcasing their vocal abilities and captivating audiences with their performances. These reality TV competitions not only provided a platform for undiscovered talent but also played a significant role in shaping popular music trends and influencing the music industry.</p>
            <p>Furthermore, reality TV shows like "Making the Band" and "The Pussycat Dolls Present: The Search for the Next Doll" showcased the behind-the-scenes process of forming musical groups, offering viewers a glimpse into the challenges and triumphs of aspiring artists. "Making the Band" famously chronicled the creation of musical acts like O-Town and Danity Kane, while "The Pussycat Dolls Present" aimed to assemble the next member of the popular girl group. These shows not only entertained audiences but also highlighted the rigorous training and dedication required to succeed in the competitive world of pop music. Overall, reality TV shows played a significant role in shaping the pop music landscape of the 2000s, contributing to the discovery of new talent and the creation of chart-topping hits.</p>"""
        )

        lesson14 = Lesson(
            language_id="2",
            topic_id="4",
            course_id="6",
            title="The magic of Greek cuisine",
            prev_lesson="",
            next_lesson="15",
            lesson_type="reading",
            content="""<p lang='el-GR'>Η Μαγεία της Ελληνικής Κουζίνας: Η Ελληνική κουζίνα είναι γνωστή για την ποικιλία και τη γεύση των πιάτων της. Ένα από τα πιο δημοφιλή πιάτα είναι η μουσακάς, μια εκλεκτή συνταγή με αιγοπρόβειο κιμά, ντομάτες, μελιτζάνες και λαχανικά, όλα φιλέτα με τριμμένο τυρί κασέρι. Μια μουσακάς φτιαγμένη με προσοχή και αγάπη είναι μια αληθινή απόλαυση για τον ουρανίσκο.</p><p lang='el-GR'>Ένα άλλο δημοφιλές πιάτο είναι οι σουβλάκια, κομμάτια κρέατος που ψήνονται σε ξύλινες σούβλες και σερβίρονται με ψωμί πίτα, τζατζίκι, τομάτα, και κρεμμύδι. Τα σουβλάκια είναι ιδανικά για ένα γεύμα στο δρόμο ή για ένα γλέντι με φίλους.</p>"""
        )

        lesson15 = Lesson(
            language_id="2",
            topic_id="4",
            course_id="6",
            title="The mystical story of moussaka",
            prev_lesson="14",
            next_lesson="16",
            lesson_type="reading",
            content="""<p lang='el-GR'>Η Μυστική Ιστορία της Μουσακάς: Η μουσακάς είναι ένα από τα πιο αγαπημένα πιάτα της Ελληνικής κουζίνας, αλλά η ιστορία της είναι εξίσου γευστική όσο και ενδιαφέρουσα. Το όνομά της προέρχεται από τον τουρκικό όρο "μουσακά", που σημαίνει "χωρίς αλάτι". Ωστόσο, η πραγματική της προέλευση είναι αμφίρροπη και συνδέεται με τις παραδόσεις των Βαλκανίων.</p><p lang='el-GR'>Η μουσακάς συνήθως περιλαμβάνει φρεσκοκομμένες μελιτζάνες, κιμά αρνιού ή μοσχαρίσιο, ντομάτες, κρεμμύδια, και μπεσαμέλ. Η παραδοσιακή μέθοδος μαγειρέματος περιλαμβάνει το ψήσιμο των μελιτζάνων πριν την προσθήκη στο πιάτο, προσδίδοντας τους μια μοναδική γεύση και υφή. Συνήθως σερβίρεται ζεστή, συνοδευόμενη με ντομάτα ή κρεμμύδι και παραδοσιακό ελληνικό γιαούρτι.</p>"""
        )

        lesson16 = Lesson(
            language_id="2",
            topic_id="4",
            course_id="6",
            title="Souvlaki",
            prev_lesson="15",
            next_lesson="17",
            lesson_type="reading",
            content="""<p lang='el-GR'>Η Μαγεία του Σουβλακίου: Στην ελληνική κουζίνα, ένα από τα πιο δημοφιλή πιάτα είναι το σουβλάκι. Το σουβλάκι έχει αρχές που χρονολογούνται αιώνες πίσω, όταν οι αρχαίοι Έλληνες χρησιμοποιούσαν τις σούβλες για να ψήσουν κρέας. Σήμερα, το σουβλάκι συνήθως περιλαμβάνει κομμάτια κρέατος, όπως χοιρινό, κοτόπουλο ή αρνί, που ψήνονται σε ξύλινες σούβλες και σερβίρονται με ψωμί πίτα, τζατζίκι, τομάτα και κρεμμύδι.</p><p lang='el-GR'>Το καλύτερο σουβλάκι στην Ελλάδα συχνά θεωρείται αυτό που προετοιμάζεται με παραδοσιακούς τρόπους ψησίματος και με υλικά υψηλής ποιότητας. Οι καλύτεροι σεφ και σουβλατζήδες γνωρίζουν τη σημασία της προετοιμασίας και της ψήσιμας στον ξυλόφουρνο για να δώσουν στο σουβλάκι τον αυθεντικό του χαρακτήρα και γεύση.</p>"""
        )

        lesson17 = Lesson(
            language_id="2",
            topic_id="4",
            course_id="6",
            title="The beloved Greek Salad",
            prev_lesson="16",
            next_lesson="22",
            lesson_type="reading",
            content="""<p lang='el-GR'>Η Αγαπημένη Ελληνική Σαλάτα: Η Ελληνική σαλάτα είναι ένα από τα πιο διάσημα πιάτα της ελληνικής κουζίνας. Η ιστορία της ξεκινά αιώνες πίσω, όταν οι αρχαίοι Έλληνες απόλαμβαναν απλές σαλάτες από τα φρέσκα λαχανικά και τα τυριά της χώρας τους. Η σύνθεσή της είναι απλή: ντομάτες, αγγούρια, πιπεριές, κρεμμύδια, φέτα, ελιές και ελαιόλαδο, όλα φιλέτα και απολαυστικά.</p><p lang='el-GR'>Η παραδοσιακή ελληνική σαλάτα είναι διάσημη για τη φρεσκάδα των συστατικών της και την απλότητα της παρασκευής της. Το μυστικό της είναι η χρήση υψηλής ποιότητας υλικών και η σεβασμός προς την παράδοση. Αυτό το αγαπημένο πιάτο έχει γίνει τόσο γνωστό και δημοφιλές σε άλλες χώρες λόγω της γεύσης του, της υγιεινής του διατροφικής αξίας και της εύκολης παρασκευής του.<p>"""
        )

        lesson18 = Lesson(
            language_id="2",
            topic_id="4",
            course_id="7",
            title="Greek desserts",
            prev_lesson="",
            next_lesson="19",
            lesson_type="reading",
            content="""<p lang='el-GR'>Η Γλυκιά Παράδοση της Ελληνικής Κουζίνας: Στην ελληνική κουζίνα, η παράδοση των γλυκών και των επιδορπίων είναι πλούσια και πολύχρωμη. Από τον παραδοσιακό γαλακτομπούρεκο μέχρι το δροσερό γιαούρτι με μέλι και καρύδια, τα ελληνικά γλυκά αποτελούν μια αναπόσπαστη μέρος της κουλτούρας μας.</p><p lang='el-GR'>Ένα από τα δημοφιλή ελληνικά γλυκά είναι οι κουλουράκια, μικρά γλυκά με τυρί και κανέλα που συνοδεύουν τέλεια τον καφέ ή το τσάι. Άλλο ένα αγαπημένο είναι το γαλακτομπούρεκο, μια παραδοσιακή γλυκιά πίτα με φύλλο και γεμίση από γάλα, αυγά και ζάχαρη. Με την προσθήκη κανέλας και σιροπιού, γίνεται ακόμα πιο γευστικό.<p>"""
        )
        
        lesson19 = Lesson(
            language_id="2",
            topic_id="4",
            course_id="7",
            title="The origin of Baklava",
            prev_lesson="18",
            next_lesson="20",
            lesson_type="reading",
            content="""<p lang='el-GR'>Η Γλυκιά Ιστορία του Μπακλαβά: Κάποτε, σε ένα μικρό χωριό της Ανατολικής Μεσογείου, ζούσε μια γενναία γυναίκα με το όνομα Αρετή. Η Αρετή ήταν γνωστή σε ολόκληρο το χωριό για τις μοναδικές της ικανότητες στη μαγειρική, και ιδιαίτερα στην παρασκευή γλυκών.</p><p lang='el-GR'>Μια μέρα, καθώς περπατούσε στα στενά του χωριού, η Αρετή συνάντησε έναν ταξιδιώτη από την Περσία, ο οποίος της μίλησε για ένα νέο είδος γλυκού που ονομαζόταν "μπακλαβάς". Προκειμένου να μάθει τη συνταγή, η Αρετή δέχτηκε να βοηθήσει τον ταξιδιώτη να περάσει τη νύχτα στο σπίτι της και να μοιραστεί τις γνώσεις του. Μετά από ατελείωτες ώρες στην κουζίνα, η Αρετή και ο ταξιδιώτης παρουσίασαν ένα εκπληκτικό, αρωματικό μπακλαβά που έγινε αμέσως αγαπημένο σε ολόκληρο το χωριό.<p>"""
        )
        
        lesson20 = Lesson(
            language_id="2",
            topic_id="4",
            course_id="7",
            title="Sweet smell of bougatsa",
            prev_lesson="19",
            next_lesson="20",
            lesson_type="reading",
            content="""<p lang='el-GR'>Στους περισσότερους ελληνικούς δρόμους, μια οικεία μυρωδιά αναδεικνύει την έναρξη μιας νέας ημέρας. Είναι η μυρωδιά της μπουγάτσας, ενός αγαπημένου ελληνικού γλυκού που φτιάχνεται από λεπτές φύλλο πίτας και γεμίζεται με γάλα, κρέμα και άλλα νόστιμα υλικά.</p><p lang='el-GR'>Η παρασκευή της μπουγάτσας είναι ένας πολύπλοκος και χρονοβόρος διαδικασία. Οι μάστορες της μπουγάτσας, γνώστες του μυστικού της επιτυχίας, λαμβάνουν μεγάλη προσοχή σε κάθε λεπτομέρεια της παρασκευής. Η γεύση της κρούστας πρέπει να είναι τραγανή και η γέμιση πρέπει να είναι πλούσια και κρεμώδης.</p>"""
        )
        
        lesson21 = Lesson(
            language_id="2",
            topic_id="4",
            course_id="7",
            title="Koulourakia: a sweet, traditional pastry",
            prev_lesson="20",
            next_lesson="",
            lesson_type="reading",
            content="""<p lang='el-GR'>Τα Μυστικά των Κουλουρακιών: Σε ένα μικρό χωριό κοντά στη Θεσσαλονίκη, ζούσε μια γλυκιά γιαγιά με το όνομα Ελένη. Η Ελένη ήταν γνωστή σε ολους για τις μοναδικές της ικανότητες στη μαγειρική, και ιδιαίτερα για την παρασκευή των κουλουρακιών.</p><p lang='el-GR'>Κάθε Παρασκευή, η Ελένη άρχιζε να φτιάχνει τα κουλουράκια της. Χρησιμοποιούσε τα καλύτερα υλικά και ακολουθούσε μια παλιά, μυστική συνταγή που κληρονόμησε από τη μητέρα της. Όλοι οι γείτονες περίμεναν ανυπόμονα να δοκιμάσουν τα νόστιμα κουλουράκια της Ελένης.</p>"""
        )

        lesson22 = Lesson(
            language_id="2",
            topic_id="4",
            course_id="6",
            title="Discovering the best spanakopita in Athens",
            prev_lesson="17",
            next_lesson="",
            lesson_type="reading",
            content="""<p lang='el-GR'>Ανακάλυψη των Καλύτερων Σπανακόπιτων στην Αθήνα: Μια νέα έρευνα από την Ένωση Γαστρονομίας της Αθήνας αποκάλυψε τις καλύτερες σπανακόπιτες στην πόλη. Μετά από μήνες δοκιμών και αξιολογήσεων από έμπειρους γευσιγνώστες, οι ειδικοί κατέληξαν σε μια λίστα των κορυφαίων μαγαζιών που προσφέρουν την πιο λαχταριστή σπανακόπιτα στην πόλη.</p><p lang='el-GR'>Ανάμεσα στους νικητές περιλαμβάνονται τα παραδοσιακά φούρνου της πλατείας Μοναστηρακίου, το γνωστό εστιατόριο στην πλατεία Συντάγματος και ένα μικρό κρυφό μαγαζί στην περιοχή της Πλάκας. Οι πελάτες έχουν ενθουσιαστεί με την ποιότητα και τη φρεσκάδα των υλικών που χρησιμοποιούνται σε αυτά τα μέρη.</p>"""
        )

        lessons = [ lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8, lesson9, lesson10, lesson11, lesson12, lesson13, lesson14, lesson15, lesson16, lesson17, lesson18, lesson19, lesson20, lesson21, lesson22]
        db.session.add_all(lessons)
        db.session.commit()

        print("Seeding questions...")

        question1 = Question(
            lesson_id=1,
            question_text="Write a paragraph describing your favorite Bossa Nova song. What is it about? Who is the artist? When was it released? What do you like about it?"
        )
        question2 = Question(
            lesson_id=2,
            question_text="Write a paragraph describing your favorite Funk song. What is it about? Who is the artist? When was it released? What do you like about it?"
        )

        question3 = Question(
            lesson_id=14,
            question_text="Η ελληνική κουζίνα είναι γεμάτη από υπέροχες γεύσεις και παραδοσιακές συνταγές. Ποια είναι η αγαπημένη σας συνταγή από την ελληνική κουζίνα και γιατί;"
        )

        question4 = Question(
            lesson_id=15,
            question_text="Ποια είναι η προσωπική σας εμπειρία με τη μουσακάς; Έχετε δοκιμάσει να τη μαγειρέψετε στο σπίτι;"
        )

        question5 = Question(
            lesson_id=16,
            question_text="Ποια είναι η αγαπημένη σας μνήμη ή εμπειρία με σουβλάκι; Τι θεωρείτε ότι κάνει ένα σουβλάκι τόσο ξεχωριστό στην ελληνική κουζίνα;"
        )

        question6 = Question(
            lesson_id=17,
            question_text="Ποια είναι η αγαπημένη σας μνήμη ή εμπειρία με την ελληνική σαλάτα; Τι πιστεύετε ότι κάνει αυτήν τη σαλάτα τόσο αγαπημένη σε πολλές χώρες παγκοσμίως;"
        )
        
        question7 = Question(
            lesson_id=18,
            question_text="Έχετε δοκιμάσει ποτέ κάποιο παραδοσιακό ελληνικό γλυκό; Ποιό απ'όλα; Ή ποιο γλυκό θα θέλατε να δοκιμάσετε;"
        )
        
        question8 = Question(
            lesson_id=19,
            question_text="Πώς νομίζετε ότι η Αρετή επηρεάστηκε από τη συνάντησή της με τον ταξιδιώτη από την Περσία;"
        )

        question9 = Question(
            lesson_id=20,
            question_text="Στην Ελλάδα, υπάρχουν πολλά μέρη όπου μπορείς να βρεις την καλύτερη μπουγάτσα. Ποια είναι η αγαπημένη σας περιοχή για να απολαύσετε μια νόστιμη μπουγάτσα; Και πώς πιστεύετε ότι η μπουγάτσα συμβάλλει στην ελληνική κουλτούρα;"
        )
        
        question10 = Question(
            lesson_id=21,
            question_text="Η παρασκευή των κουλουρακιών ήταν πάντα μια γιορτινή αφορμή για το χωριό. Πώς νομίζετε ότι η Ελένη κατάφερε να φτιάξει τα πιο νόστιμα κουλουράκια;"
        )

        question11 = Question(
            lesson_id=22,
            question_text="Ποιο είναι το αγαπημένο σας μέρος για να απολαύσετε μια νόστιμη σπανακόπιτα στην Αθήνα; Και ποιες είναι οι αγαπημένες σας γεύσεις;"
        )

        questions = [ question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11 ]

        db.session.add_all(questions)
        db.session.commit()

        print("Done seeding!")