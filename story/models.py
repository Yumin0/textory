from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class StoryAuthor(models.Model):
    """
    Model representing a author.
    """
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    #bio = models.TextField(max_length=400, help_text="Enter your bio details here.")

    def get_absolute_url(self):
        """
        Returns the url to access a particular story_author instance.
        """

        return reverse('storys_by_author', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.username

#class Tag(models.Model):
#    name = models.CharField(max_length=20)
#    slug = models.SlugField(unique=True)

#    def __str__(self):
#        return self.name

#    def get_absolute_url(self):
#        return reverse('story:tag_detail', kwargs={'tag_name': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ThingAdjective(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Story(models.Model):
    author = models.ForeignKey(StoryAuthor, related_name='storys',null=True)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='storys',null=True)
    #author = models.ForeignKey(User, related_name='storys',null=True)

    category = models.ForeignKey(Category,null=True)

    adjective_t = models.ForeignKey(ThingAdjective,null=True)
    likes = models.PositiveIntegerField(default=0)

    @property
    def total_likes(self):
        return self.likes.count()

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='story_liked',
                                        blank=True)

    sb_thing = models.CharField(max_length=50,null=True)
    sb_story = models.CharField(max_length=150,null=True)
    sb_name = models.CharField(max_length=30,null=True)

    #create_at = models.DateTimeField(auto_now_add=True,null=True)
#    tags = models.ManyToManyField(Tag, blank=True, related_name='tags_story')
    #tags = models.CharField('Tag', blank=True)




    SB_GENDER = (
        ('他','他'),
        ('她','她'),
        ('它','它'),
    )
    sb_gender = models.CharField(max_length = 100,null=True,choices = SB_GENDER, )

    SB_ADV = (
        ('有點','有點'),
        ('非常','非常'),
        ('蠻','蠻'),
        ('超級','超級'),
        ('史上無敵','史上無敵'),
    )
    sb_adv = models.CharField(max_length = 100,null=True,choices = SB_ADV)

    SB_ADJ = (
        ('humor','humor'),
        ('奇怪','奇怪'),
        ('白目','白目'),
        ('白痴','白痴'),
        ('有病','有病'),
        ('自戀','自戀'),
        ('搞笑','搞笑'),
        ('孤僻','孤僻'),
        ('嚴肅','嚴肅'),
        ('無趣','無趣'),
        ('奇耙','奇耙'),
        ('可怕','可怕'),
        ('笨蛋','笨蛋'),
        ('健忘','健忘'),
        ('厲害','厲害'),
        ('正常','正常'),
        ('懶惰','懶惰'),
    )
    sb_adj = models.CharField(max_length = 100,null=True,choices = SB_ADJ)

    SB_ABOUT = (
        ('很喜歡','很喜歡'),
        ('不喜歡','不喜歡'),
        ('不吃','不吃'),
        ('討厭','討厭'),
        ('怕','怕'),
        ('常常','常常'),
        ('很會','很會'),
        ('曾經','曾經'),
    )
    sb_about = models.CharField(max_length = 100,null=True,choices = SB_ABOUT)

    WHO = (
        ('我們','我們'),
        ('他','他'),
        ('她','她'),
        ('它','它'),
    )
    who = models.CharField(max_length = 100,null=True,choices = WHO)

    STH_ADJ = (
        ('扯','扯'),
        ('蠢','蠢'),
        ('煩','煩'),
        ('北七','北七'),
        ('北爛','北爛'),
        ('誇張','誇張'),
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
        ('嘿丟','嘿丟'),
    )
    itjcts = models.CharField(max_length = 100,null=True,choices = ITJCTS)

    MARK = (
        ('~','~'),
        ('!','!'),
        ('!!!','!!!'),
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

    def get_like_url(self):
        return reverse("storys:like-toggle", kwargs={"slug": self.slug})

    def get_api_like_url(self):
        return reverse("posts:like-api-toggle", kwargs={"slug": self.slug})
