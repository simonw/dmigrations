from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `blog_category` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(255) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `blog_category_entries` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `category_id` integer NOT NULL,
        `entry_id` integer NOT NULL,
        UNIQUE (`category_id`, `entry_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `blog_category_entries` ADD CONSTRAINT category_id_refs_id_8bfa9be FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`id`);
""", """
    ALTER TABLE `blog_category_entries` ADD CONSTRAINT entry_id_refs_id_df19365 FOREIGN KEY (`entry_id`) REFERENCES `blog_entry` (`id`);
"""], sql_down=["""
    DROP TABLE `blog_category_entries`;
""", """
    DROP TABLE `blog_category`;
"""])
