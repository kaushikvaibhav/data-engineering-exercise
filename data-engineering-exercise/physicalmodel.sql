CREATE TABLE book(
  "book_key" varchar(15) NOT NULL PRIMARY KEY,
  "title" varchar(50) NOT NULL,
  "edition_count" int,
  "cover_id" int,
  "cover_edition_key" varchar(15),
  "lendinglibrary" boolean DEFAULT false,
  "printdisabled" boolean DEFAULT false,
  "lending_edition" varchar(15),
  "lending_identifier" varchar(50),
  "first_publish_year" int,
  "status" varchar(20),
  "last_modified_timestamp" DATETIME,
  "creation_timestamp" DATETIME
);

Create Table authors(
  "author_name" varchar(50),
  "last_modified_value" DATETIME,
  "author_key" varchar(15) NOT NULL PRIMARY KEY,
  "creation_timestamp" DATETIME
);

Create Table book_author(
  "author_key" varchar(15) NOT NULL,
  "book_key" varchar(15) NOT NULL
)