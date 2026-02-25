from django.utils.text import slugify
def slugify_article(instance,newSlug=None):
    slug = slugify(instance.title)
    if newSlug:
        slug = newSlug
    Klass = instance.__class__
    qs = Klass.objects.filter(slug = slug).exclude(id=instance.id)
    if qs.exists():
        if newSlug:
            slug = slug.split("-")
            last = int(slug.pop())
            slug = "-".join(slug)
            slug = f'{slug}-{last+1}'
        else:
            slug = f'{slug}-{qs.count()+1}'
        return slugify_article(instance,slug)
    instance.slug = slug