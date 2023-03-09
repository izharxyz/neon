-- CreateTable
CREATE TABLE "Post" (
    "id" INT8 NOT NULL DEFAULT unique_rowid(),
    "title" STRING NOT NULL,
    "content" STRING NOT NULL,

    CONSTRAINT "Post_pkey" PRIMARY KEY ("id")
);
