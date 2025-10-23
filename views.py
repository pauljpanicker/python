blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

for x in blog_views:
    if x>1000:
        print("the view is trending")
    elif 500 <=x>= 1000:
        print("the view is average")
    else:
        print("low traffic")
total=(sum(blog_views))
print("the sum of the view:"+str(total))
trending_count=len([x for x in blog_views if x>1000])
print("trending view:",trending_count)
