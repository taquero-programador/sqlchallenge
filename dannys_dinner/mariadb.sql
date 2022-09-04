-- tabla members
CREATE TABLE `bender`.`members` (
    `customer_id` VARCHAR(1) NOT NULL ,
    `join_date` DATETIME NOT NULL ,
    PRIMARY KEY (`customer_id`)) ENGINE = InnoDB;

-- tabla menu
CREATE TABLE `bender`.`menu` (
    `product_id` INT NOT NULL AUTO_INCREMENT ,
    `product_name` VARCHAR(30) NOT NULL ,
    `price` INT NOT NULL , PRIMARY KEY (`product_id`)) ENGINE = InnoDB; 

-- tabla sales
CREATE TABLE `bender`.`sales` (
    `customer_id` VARCHAR(1) NOT NULL ,
    `order_date` DATE NOT NULL ,
    `product_id` INT NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES `bender`.`member`(customer_id),
    FOREIGN KEY(product_id) REFERENCES `bender`.`menu`(product_id)
) ENGINE = InnoDB;
