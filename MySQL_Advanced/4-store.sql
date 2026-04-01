-- Crea un trigger que reduce la cantidad de un item después de agregar una nueva orden
CREATE TRIGGER order_decrease BEFORE INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
