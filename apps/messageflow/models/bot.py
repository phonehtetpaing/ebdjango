from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Scenario(models.Model):
    """
    Scenario that holds a sequence of messages
    """
    name = models.CharField(null=False, max_length=256)

    owner_id = models.IntegerField('owner_id', null=False)
    app_id = models.CharField('app_id', null=False, max_length=256)
    regist_dt = models.DateTimeField('regist datetime', null=False, auto_now_add=True)

    class Meta:
        verbose_name = "Scenario"
        permissions = ()

    def __str__(self):
        return self.name

    @property
    def start_block(self):
        return self.message_block_set.order_by('display_order').first()


class Bot(models.Model):
    """
    Bot that fires off a message scenario sequence
    """
    name = models.CharField(null=False, max_length=256)
    scenario = models.ManyToManyField(Scenario, through='BotScenario')
    is_active = models.BooleanField('active flg', default=False)
    owner_id = models.IntegerField('owner_id', null=False)
    app_id = models.CharField('app_id', null=False, max_length=256)
    regist_dt = models.DateTimeField('regist datetime', null=False, auto_now_add=True)

    class Meta:
        verbose_name = "Bot"
        permissions = ()

    def __str__(self):
        return self.name


class BotScenario(models.Model):
    """
    Link class between Bots and Scenario
    """
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE, null=False, blank=False)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, null=False, blank=False)
    weight = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    class Meta:
        verbose_name = "BotScenario"
        permissions = ()

    def __str__(self):
        return "Bot:{0}-Scenario:{1}".format(self.bot, self.scenario)
