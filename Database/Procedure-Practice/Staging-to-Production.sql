/*
Viết một procedure tên process_staged_sales() để chuyển dữ liệu bán hàng từ bảng tạm staging_sales sang bảng chính production_sales, 
đồng thời xử lý các bản ghi lỗi.

Toàn bộ quá trình phải là một giao dịch duy nhất. Nếu có lỗi, tất cả các thay đổi phải được hủy bỏ.

Logic xử lý cho mỗi dòng trong staging_sales:

    Kiểm tra xem product_code có tồn tại trong bảng products không và sale_price có lớn hơn 0 không.

    Nếu hợp lệ:
        Chuyển đổi product_code thành product_id.
        Tính total_revenue (quantity * sale_price).
        Chèn dòng dữ liệu đã chuẩn hóa vào production_sales.

    Nếu không hợp lệ:
        Ghi một dòng vào error_log với thông báo lỗi và id của dữ liệu gốc.
        óa dòng đã được xử lý khỏi staging_sales.

------------------- Cấu trúc các bảng ---------------------
Table: staging_sales
+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| id           | int      |
| product_code | varchar  |
| quantity     | int      |
| sale_price   | decimal  |
| sale_date    | date     |
+--------------+----------+

Table: production_sales
+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| id            | int      |
| product_id    | int      |
| quantity      | int      |
| total_revenue | decimal  |
| sale_date     | date     |
+---------------+----------+

Table: products
+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| id           | int      |
| product_code | varchar  |
| product_name | varchar  |
+--------------+----------+

Table: error_log
+---------------+-----------+
| Column Name   | Type      |
+---------------+-----------+
| id            | int       |
| error_message | text      |
| raw_data_id   | int       |
| logged_at     | timestamp |
+---------------+-----------+
*/

CREATE OR REPLACE PROCEDURE process_staged_sales()
LANGUAGE plpgsql
as $$
DECLARE 
    correct_product_id INT;
    staged_row record;
BEGIN 
    FOR staged_row IN SELECT * FROM staging_sales LOOP
        SELECT id INTO correct_product_id FROM products WHERE products.product_code=staged_row.product_code;
        IF correct_product_id IS NULL THEN
            INSERT INTO error_log(error_message, raw_data_id, logged_at) VALUES ('Product is not Exist', staged_row.id, NOW());
        ELSIF staged_row.sale_price <= 0 THEN 
            INSERT INTO error_log(error_message,raw_data_id,logged_at) VALUES('Price did not correct', staged_row.id, NOW());

        ELSE
            INSERT INTO production_sales(product_id,quantity,total_revenue,sale_date) VALUES (correct_product_id, staged_row.quantity, staged_row.quantity*staged_row.sale_price, staged_row.sale_date);
        END IF; 
        DELETE FROM staging_sales WHERE id=staged_row.id;
    END LOOP;
    COMMIT;
END;
$$;