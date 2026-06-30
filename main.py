# 1. Endpoint hiện tại có Path Parameter không?
# -> Có, endpoint hiện tại đã khai báo chính xác Path Parameter.

# 2. Path Parameter trong bài này là gì?
# -> Tham số đường dẫn trong bài này là {status}.

# 3. Khi gọi /orders/status/pending, biến status nhận giá trị gì?
# -> Biến status nhận giá trị là chuỗi dữ liệu (string): "pending".

# 4. Vì sao API hiện tại trả về sai dữ liệu?
# -> Vì hàm xử lý nhận giá trị biến status từ URL nhưng không thực hiện logic 
#    lọc (filter) danh sách đơn hàng theo trạng thái này.

# 5. Dòng code nào đang khiến API bỏ qua giá trị status?
# -> Dòng code: return orders
# -> Dòng này trả trực tiếp toàn bộ mảng orders ban đầu mà không qua bộ lọc.

from fastapi import FastAPI, HTTPException

app = FastAPI()

orders = [
    {"id": 1, "customer_name": "Nguyễn Văn An", "total": 250000, "status": "pending"},
    {"id": 2, "customer_name": "Trần Thị Bình", "total": 500000, "status": "paid"},
    {"id": 3, "customer_name": "Lê Văn Cường", "total": 150000, "status": "cancelled"},
    {"id": 4, "customer_name": "Phạm Thị Dung", "total": 320000, "status": "pending"}
]


valid_statuses = ["pending", "paid", "cancelled"]

@app.get("/orders/status/{status}")
def get_orders_by_status(status: str):
    if status not in valid_statuses:
        raise HTTPException(
            status_code=400, 
            detail= "Trạng thái đơn hàng không hợp lệ"
        )
    
    filtered_orders = []
    for o in orders:
        if o["status"] == status:
            filtered_orders.append(o)
            
    return filtered_orders
