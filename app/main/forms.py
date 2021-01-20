from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, ValidationError, RadioField, SelectMultipleField
from wtforms.fields.simple import HiddenField
from wtforms.validators import DataRequired, Email, Length, Regexp
from flask_pagedown.fields import PageDownField
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class AddDogForm(FlaskForm):
    name = StringField('Nickname', validators=[DataRequired(), Length(1, 64)])
    breed = SelectField('Breed', choices=['Afador', 'Affenhuahua', 'Affenpinscher', 'Afghan Hound', 'Airedale Terrier', 'Akbash', 'Akita', 'Akita Chow', 'Akita Pit', 'Akita Shepherd', 'Alaskan Klee Kai', 'Alaskan Malamute', 'American Bulldog', 'American English Coonhound', 'American Eskimo Dog', 'American Foxhound', 'American Hairless Terrier', 'American Leopard Hound', 'American Pit Bull Terrier', 'American Pugabull', 'American Staffordshire Terrier', 'American Water Spaniel', 'Anatolian Shepherd Dog', 'Appenzeller Sennenhunde', 'Auggie', 'Aussiedoodle', 'Aussiepom', 'Australian Cattle Dog', 'Australian Kelpie', 'Australian Retriever', 'Australian Shepherd', 'Australian Shepherd Husky', 'Australian Shepherd Lab Mix', 'Australian Shepherd Pit Bull Mix', 'Australian Stumpy Tail Cattle Dog', 'Australian Terrier', 'Azawakh', 'Barbet', 'Basenji', 'Bassador', 'Basset Fauve de Bretagne', 'Basset Hound', 'Basset Retriever', 'Bavarian Mountain Scent Hound', 'Beabull', 'Beagle', 'Beaglier', 'Bearded Collie', 'Bedlington Terrier', 'Belgian Malinois', 'Belgian Sheepdog', 'Belgian Tervuren', 'Bergamasco Sheepdog', 'Berger Picard', 'Bernedoodle', 'Bernese Mountain Dog', 'Bichon Frise', 'Biewer Terrier', 'Black and Tan Coonhound', 'Black Mouth Cur', 'Black Russian Terrier', 'Bloodhound', 'Blue Lacy', 'Bluetick Coonhound', 'Bocker', 'Boerboel', 'Boglen Terrier', 'Bohemian Shepherd', 'Bolognese', 'Borador', 'Border Collie', 'Border Sheepdog', 'Border Terrier', 'Bordoodle', 'Borzoi', 'BoShih', 'Bossie', 'Boston Boxer', 'Boston Terrier', 'Boston Terrier Pekingese Mix', 'Bouvier des Flandres', 'Boxador', 'Boxer', 'Boxerdoodle', 'Boxmatian', 'Boxweiler', 'Boykin Spaniel', 'Bracco Italiano', 'Braque du Bourbonnais', 'Briard', 'Brittany', 'Broholmer', 'Brussels Griffon', 'Bugg', 'Bull-Pei', 'Bull Terrier', 'Bullador', 'Bullboxer Pit', 'Bulldog', 'Bullmastiff', 'Bullmatian', 'Cairn Terrier', 'Canaan Dog', 'Cane Corso', 'Cardigan Welsh Corgi', 'Carolina Dog', 'Catahoula Bulldog', 'Catahoula Leopard Dog', 'Caucasian Shepherd Dog', 'Cav-a-Jack', 'Cavachon', 'Cavador', 'Cavalier King Charles Spaniel', 'Cavapoo', 'Central Asian Shepherd Dog', 'Cesky Terrier', 'Chabrador', 'Cheagle', 'Chesapeake Bay Retriever', 'Chi Chi', 'Chi-Poo', 'Chigi', 'Chihuahua', 'Chilier', 'Chinese Crested', 'Chinese Shar-Pei', 'Chinook', 'Chion', 'Chipin', 'Chiweenie', 'Chorkie', 'Chow Chow', 'Chow Shepherd', 'Chug', 'Chusky', 'Cirneco dell’Etna', 'Clumber Spaniel', 'Cockalier', 'Cockapoo', 'Cocker Spaniel', 'Collie', 'Corgi Inu', 'Corgidor', 'Corman Shepherd', 'Coton de Tulear', 'Croatian Sheepdog', 'Curly-Coated Retriever', 'Dachsador', 'Dachshund', 'Dalmatian', 'Dandie Dinmont Terrier', 'Daniff', 'Danish-Swedish Farmdog', 'Deutscher Wachtelhund', 'Doberdor', 'Doberman Pinscher', 'Docker', 'Dogo Argentino', 'Dogue de Bordeaux', 'Dorgi', 'Dorkie', 'Doxiepoo', 'Doxle', 'Drentsche Patrijshond', 'Drever', 'Dutch Shepherd', 'English Cocker Spaniel', 'English Foxhound', 'English Setter', 'English Springer Spaniel', 'English Toy Spaniel', 'Entlebucher Mountain Dog', 'Estrela Mountain Dog', 'Eurasier', 'Field Spaniel', 'Fila Brasileiro', 'Finnish Lapphund', 'Finnish Spitz', 'Flat-Coated Retriever', 'Fox Terrier', 'French Bulldog', 'French Bullhuahua', 'French Spaniel', 'Frenchton', 'Frengle', 'German Longhaired Pointer', 'German Pinscher', 'German Shepherd Dog',
                                          'German Shepherd Pit Bull', 'German Shepherd Rottweiler Mix', 'German Sheprador', 'German Shorthaired Pointer', 'German Spitz', 'German Wirehaired Pointer', 'Giant Schnauzer', 'Glen of Imaal Terrier', 'Goberian', 'Goldador', 'Golden Cocker Retriever', 'Golden Mountain Dog', 'Golden Retriever', 'Golden Retriever Corgi', 'Golden Shepherd', 'Goldendoodle', 'Gollie', 'Gordon Setter', 'Great Dane', 'Great Pyrenees', 'Greater Swiss Mountain Dog', 'Greyador', 'Greyhound', 'Hamiltonstovare', 'Hanoverian Scenthound', 'Harrier', 'Havanese', 'Hokkaido', 'Horgi', 'Hovawart', 'Huskita', 'Huskydoodle', 'Ibizan Hound', 'Icelandic Sheepdog', 'Irish Red And White Setter', 'Irish Setter', 'Irish Terrier', 'Irish Water Spaniel', 'Irish Wolfhound', 'Italian Greyhound', 'Jack-A-Poo', 'Jack Chi', 'Jack Russell Terrier', 'Jackshund', 'Japanese Chin', 'Japanese Spitz', 'Korean Jindo Dog', 'Kai Ken', 'Karelian Bear Dog', 'Keeshond', 'Kerry Blue Terrier', 'King Shepherd', 'Kishu Ken', 'Komondor', 'Kooikerhondje', 'Kuvasz', 'Kyi-Leo', 'Lab Pointer', 'Labernese', 'Labmaraner', 'Labrabull', 'Labradane', 'Labradoodle', 'Labrador Retriever', 'Labrastaff', 'Labsky', 'Lagotto Romagnolo', 'Lakeland Terrier', 'Lancashire Heeler', 'Leonberger', 'Lhasa Apso', 'Lhasapoo', 'Lowchen', 'Maltese', 'Maltese Shih Tzu', 'Maltipoo', 'Manchester Terrier', 'Mastador', 'Mastiff', 'Miniature Pinscher', 'Miniature Schnauzer', 'Morkie', 'Mudi', 'Mutt (Mixed)', 'Neapolitan Mastiff', 'Newfoundland', 'Norfolk Terrier', 'Northern Inuit Dog', 'Norwegian Buhund', 'Norwegian Elkhound', 'Norwegian Lundehund', 'Norwich Terrier', 'Nova Scotia Duck Tolling Retriever', 'Old English Sheepdog', 'Otterhound', 'Papillon', 'Papipoo', 'Patterdale Terrier', 'Peekapoo', 'Pekingese', 'Pembroke Welsh Corgi', 'Petit Basset Griffon Vendéen', 'Pharaoh Hound', 'Pitsky', 'Plott', 'Pocket Beagle', 'Pointer', 'Polish Lowland Sheepdog', 'Pomapoo', 'Pomchi', 'Pomeagle', 'Pomeranian', 'Pomsky', 'Poochon', 'Poodle', 'Portuguese Podengo Pequeno', 'Portuguese Sheepdog', 'Portuguese Water Dog', 'Pug', 'Pugalier', 'Puggle', 'Puginese', 'Puli', 'Pyredoodle', 'Pyrenean Mastiff', 'Pyrenean Shepherd', 'Rat Terrier', 'Redbone Coonhound', 'Rhodesian Ridgeback', 'Rottador', 'Rottle', 'Rottweiler', 'Saint Berdoodle', 'Saint Bernard', 'Saluki', 'Samoyed', 'Samusky', 'Schipperke', 'Schnoodle', 'Scottish Deerhound', 'Scottish Terrier', 'Sealyham Terrier', 'Sheepadoodle', 'Shepsky', 'Shetland Sheepdog', 'Shiba Inu', 'Shichon', 'Shih-Poo', 'Shih Tzu', 'Shiloh Shepherd', 'Shiranian', 'Shollie', 'Shorkie', 'Siberian Husky', 'Silken Windhound', 'Silky Terrier', 'Skye Terrier', 'Sloughi', 'Small Munsterlander Pointer', 'Soft Coated Wheaten Terrier', 'Spanish Mastiff', 'Spinone Italiano', 'Springador', 'Stabyhoun', 'Staffordshire Bull Terrier', 'Staffy Bull Bullmastiff', 'Standard Schnauzer', 'Sussex Spaniel', 'Swedish Lapphund', 'Swedish Vallhund', 'Taiwan Dog', 'Terripoo', 'Texas Heeler', 'Tibetan Mastiff', 'Tibetan Spaniel', 'Tibetan Terrier', 'Toy Fox Terrier', 'Transylvanian Hound', 'Treeing Tennessee Brindle', 'Treeing Walker Coonhound', 'Valley Bulldog', 'Vizsla', 'Weimaraner', 'Welsh Springer Spaniel', 'Welsh Terrier', 'West Highland White Terrier', 'Westiepoo', 'Whippet', 'Whoodle', 'Wirehaired Pointing Griffon', 'Xoloitzcuintli', 'Yorkipoo', 'Yorkshire Terrier', ], validators=[DataRequired()])
    gender = RadioField('Gender',  choices=[
                        'Female', 'Male'], validators=[DataRequired()])
    description = TextAreaField('Description')
    tags = SelectField('Tags', choices=[
        'Shy,', 'Playful', 'Young', 'Puppy', 'Adult', 'Senior', 'Large', 'Medium', 'Small', 'Royal'])
    owner_id = HiddenField("Owner")
    submit = SubmitField('Submit')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(
        1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PostForm(FlaskForm):
    body = PageDownField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    body = StringField('', validators=[DataRequired()])
    submit = SubmitField('Submit')
