from django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('verje', 'verje@mail.com', 'kley2c0p')

# Update fields and then save again
user.first_name = 'Jesus'
user.last_name = 'Romero'
user.save()
