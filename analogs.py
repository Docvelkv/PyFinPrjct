import pandas as pd


def analog_get_dummies(ser_data: pd.Series) -> pd.DataFrame:
    """
    Упрощенный аналог метода get_dummies.
    Конвертирует категориальные значения в числовые.

    Args:
        ser_data (pd.Series): Объект Series из DataFrame.

    Returns:
        pd.DataFrame: Объект DataFrame
    """
    lst_val = ser_data.tolist()
    uniq_val = ser_data.unique().tolist()
    new_dict = {}
    for ik in range(len(uniq_val)):
        new_lst = []
        for jv in range(len(lst_val)):
            if uniq_val[ik] == lst_val[jv]:
                new_lst.append(1)
            else:
                new_lst.append(0)
        new_dict[uniq_val[ik]] = new_lst
    return pd.DataFrame(new_dict)
