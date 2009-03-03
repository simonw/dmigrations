from dmigrations.mysql import migrations as m
import datetime
migration = m.AddIndex('blog', 'category', 'name')
