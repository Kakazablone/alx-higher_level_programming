-- Creates the table "second_table" if it doesn't exist
CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);

-- Inserts multiple rows into the "second_table" in a single command
INSERT INTO `second_table` (`id`, `name`, `score`)
VALUES 
  (1, 'John', 10),
  (2, 'Alex', 3),
  (3, 'Bob', 14),
  (4, 'George', 8);
