-- Converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table
	CONVERT TO CHARACTER SET utf8mb4
	COLLATE ut8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table
	CHANGE name name
	VARCHAR(256)
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
-- Another way to be done:
-- USE htbn_0c_0
-- ALTER DATABASE CHARACTER SET utf8mb4
-- ALTER DATABASE COLLATE ...unicode...
-- ALTER TABLE first_table CONVERT TO
-- CHARACTER SET utf8mb4 COLLATE ...unicode...
