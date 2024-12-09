import { Table as AntdTable, TableProps } from 'antd';
import React from 'react';
import { TableValues } from './PrimaryTable.types';
import * as Styled from './PrimaryTable.styled';

type PrimaryTableProps<DataType> = {
  columns: TableProps<DataType>['columns'];
  data: DataType[];
};

export const PrimaryTable = <DataType extends TableValues>({ columns, data }: PrimaryTableProps<DataType>) => {
  return (
    <Styled.Container>
      <AntdTable<DataType> columns={columns} dataSource={data} pagination={false} bordered scroll={{ x: 100, y: '68vh' }} />
    </Styled.Container>
  );
};
