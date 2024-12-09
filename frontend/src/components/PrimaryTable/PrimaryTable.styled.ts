import styled from "styled-components";

export const Container = styled.div`
  thead .ant-table-cell {
    padding: 22px 10px 10px !important;
    font-family: Nunito Sans;
    font-weight: 800 !important;
    font-size: 14px;
    line-height: 1.36;
  }

  tbody {
    font-family: Nunito Sans;
    font-size: 14px;
    font-weight: 600;
    line-height: 1.36;
  }

  .ant-table-content table {
    border: none;
    padding-bottom: 23px;
    border-radius: 14px !important;
  }

  /* Скрываем верхние и нижние границы ячеек */
  .ant-table-thead > tr > th,
  .ant-table-tbody > tr > td {
    border-top: none !important;
    border-bottom: none !important;
  }

  /* Добавляем только правую границу для всех ячеек */
  .ant-table-cell {
    border-right: 0.6px solid #e0e0e033;
  }

  /* Убираем правую границу у последнего столбца */
  .ant-table-cell:last-child {
    border-right: none;
    border-inline-end: none !important;
  }

  /* Скругляем нижние углы контейнера таблицы */
  .ant-table-wrapper .ant-table-container {
    border-bottom-left-radius: 14px;
    border-bottom-right-radius: 14px;
    border-right: 0.6px solid #e0e0e033;
    border-bottom: 0.6px solid #e0e0e033;
    overflow: hidden;
  }
`;
