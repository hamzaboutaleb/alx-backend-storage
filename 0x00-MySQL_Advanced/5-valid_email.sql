-- trigger that resets the attribute valid_email only when the email has been changed.

DROP TRIGGER IF EXISTS valid_email
DELIMITER $$
CREATE TRIGGER valid_email
AFTER UPDATE users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email then
        SET NEW.valid_email = 0;
END $$
DELIMITER ;
