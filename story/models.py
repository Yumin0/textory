from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.forms.models import ModelMultipleChoiceField


#MY_CHOICES = (('item_key1', 'Item title 1.1'),
#              ('item_key2', 'Item title 1.2'),


#MY_CHOICES2 = ((1, 'Item title 2.1'),
#               (2, 'Item title 2.2'),







class Story(models.Model):
    author = models.ForeignKey(User, related_name='storys')

    sb_thing = models.CharField(max_length=30,null=True)
    sb_story = models.CharField(max_length=30,null=True)
    sb_name = models.CharField(max_length=30,null=True)


    #my_field = MultiSelectField(null=True,choices=MY_CHOICES)
    #my_field2 = MultiSelectField(null=True,choices=MY_CHOICES2,
    #                             max_choices=3,
    #                             max_length=3)




    SB_GENDER = (
        ('他','他'),
        ('她','她'),
    )
    sb_gender = models.CharField(max_length = 100,null=True,choices = SB_GENDER)

    SB_ADV = (
        ('有點','有點'),
        ('非常','非常'),
        ('蠻','蠻'),
        ('超級','超級'),
        ('史上無敵','史上無敵'),
    )
    sb_adv = models.CharField(max_length = 100,null=True,choices = SB_ADV)

    SB_ADJ = (
        ('奇怪','奇怪'),
        ('白目','白目'),
        ('有病','有病'),
        ('自戀','自戀'),
        ('搞笑','搞笑'),
    )
    sb_adj = models.CharField(max_length = 100,null=True,choices = SB_ADJ)

    SB_ABOUT = (
        ('很喜歡','很喜歡'),
        ('不喜歡','不喜歡'),
        ('不吃','不吃'),
        ('討厭','討厭'),
        ('怕','怕'),
        ('常常','常常'),
    )
    sb_about = models.CharField(max_length = 100,null=True,choices = SB_ABOUT)

    WHO = (
        ('我們','我們'),
        ('他','他'),
        ('她','她'),
    )
    who = models.CharField(max_length = 100,null=True,choices = WHO)

    STH_ADJ = (
        ('扯','扯'),
        ('蠢','蠢'),
        ('有趣','有趣'),
        ('好笑','好笑'),
        ('丟臉','丟臉'),
        ('瘋狂','瘋狂'),
        ('誇張','誇張'),
        ('無聊','無聊'),
        ('幼稚','幼稚'),
        ('難忘','難忘'),
        ('開心','開心'),
    )
    sth_adj = models.CharField(max_length = 100,null=True,choices = STH_ADJ)

    ITJCTS = (
        ('哎','哎'),
        ('哈哈','哈哈'),
        ('呵呵','呵呵'),
        ('顆顆','顆顆'),
    )
    itjcts = models.CharField(max_length = 100,null=True,choices = ITJCTS)

    MARK = (
        ('~','~'),
        ('!','!'),
        ('XD','XD'),
        ('>///<','>///<'),
        ('^^','^^'),
        (':)',':)'),
        ('。','。'),
    )
    mark = models.CharField(max_length = 100,null=True,choices = MARK)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.sb_name
