from django.db import models

# Create your models here.
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)

    def __str__(self):
        return self.title

class PhotoPost(models.Model):
    #CustomUserモデルの(user_id)をPhotoPostモデルを
    #1対多の関係で結びづける
    #CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        #フィールドのタイトル
        verbose_name='ユーザー',
        #ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
    #Categoryモデルの(user_id)をPhotoPostモデルを
    #1対多の関係で結びづける
    #Categoryが親でPhotoPostが子の関係となる
    category = models.ForeignKey(
        Category,
        #フィールドのタイトル
        verbose_name='カテゴリ',
        #ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.PROTECT
        )
    #タイトル用のフィールド
    title = models.CharField(
        verbose_name = "タイトル",
        max_length = 200
        )
    #コメント用のフィールド
    comment = models.TextField(
        verbose_name = "コメント"
        )
    #イメージのフィールド1
    image1 = models.ImageField(
        verbose_name = "イメージ1",
        upload_to='photos'
        )
    #イメージのフィールド2
    image2 = models.ImageField(
        verbose_name = "イメージ2",
        upload_to='photos',
        blank=True,
        null=True
        )
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name = "投稿日時",
        auto_now_add=True #日時を自動追加
        )

    def __str__(self):
        return self.title