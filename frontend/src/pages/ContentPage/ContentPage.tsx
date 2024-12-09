import React, { useMemo, useState } from 'react';
import { Header } from '../../components/Header';
import type { TabsProps } from 'antd';
import { EContentTabs } from './ContentPage.types';
import { Attendance } from './components/Attendance';
import * as Styled from './ContentPage.styled';
import { Feedback } from './components/Feedback';

export const ContentPage = () => {
  const [tab, setTab] = useState(EContentTabs.attendance);

  const tabs: TabsProps['items'] = useMemo(() =>
  ([
    {
      key: EContentTabs.сourses,
      label: 'Курсы',
    },
    {
      key: EContentTabs.attendance,
      label: 'Посещаемость',
    },
    {
      key: EContentTabs.feedback,
      label: 'Фидбэк',
    },
    {
      key: EContentTabs.export,
      label: 'Экспорт',
    },
  ]), []);

  const handleChangeTab = (newTab: string) => {
    setTab(newTab as EContentTabs);
  };

  const renderContent = () => {
    switch (tab) {
      case EContentTabs.feedback:
        return <Feedback />;

      case EContentTabs.attendance:
      default:
        return <Attendance />;
    }
  };

  return (
    <Styled.Container>
      <Header tabs={tabs} activeTab={tab} onChangeTab={handleChangeTab} />
      {renderContent()}
    </Styled.Container>
  );
};
