# Tenderhack-hackaton
## Making a service to automate participation in tender sessions

Для предсказания ближайшего последующего темпа снижения ставки сессии используется дискретная линейная аппроксимация (метод наименьших квадратов)

С помощью МНК анализируется ΔP за несколько последних Δt (параметризуется)

1. найдем средние значения точек
> <img src="https://render.githubusercontent.com/render/math?math=t^{mid}=\frac{1}{n}\sum{t_i}">

> <img src="https://render.githubusercontent.com/render/math?math=t^{mid}=\frac{1}{n}\sum{P_i}">
2. найдем коэффициенты линейной зависимости y = kx + b

> <img src="https://render.githubusercontent.com/render/math?math=k=\frac{\sum{(t_i-t^{mid})(P_i-P^{mid})}}{\sum{(t_i-t^{mid})^2}}">

> <img src="https://render.githubusercontent.com/render/math?math=b=P^{mid}-k*t^{mid}">
