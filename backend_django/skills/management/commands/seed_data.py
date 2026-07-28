from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from skills.models import Skill
from jobs.models import Job

class Command(BaseCommand):
    help = 'Seed initial data for WorkNest'

    def handle(self, *args, **options):
        User = get_user_model()
        if Skill.objects.exists():
            self.stdout.write(self.style.WARNING('Data already seeded'))
            return
        # Create some skills
        s1 = Skill.objects.create(name='Python', category='Programming', description='Python language')
        s2 = Skill.objects.create(name='React', category='Frontend', description='React.js')
        # Create sample users
        u1 = User.objects.create_user(email='alice@example.com', name='Alice', password='password123')
        u1.skills.add(s1)
        u2 = User.objects.create_user(email='employer@example.com', name='Employer', password='password123', role='employer')
        # Create jobs
        job = Job.objects.create(title='Backend Developer', company='Acme', description='Work on APIs', category='Software', salary={'min':50000,'max':70000,'currency':'INR','period':'monthly'}, postedBy=u2)
        job.skills.add(s1)
        self.stdout.write(self.style.SUCCESS('Seeded sample data'))
