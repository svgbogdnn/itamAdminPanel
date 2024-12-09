import React from 'react';
import * as Styled from './Header.styled';
import { Link } from '../Link';
import { HeaderLink } from '../../types';
import { ConfigProvider, Tabs } from 'antd';
import type { TabsProps } from 'antd';
import IconBell from '@src/assets/images/icon-bell.svg?react';
import { UserInfo } from './components/UserInfo';

type HeaderProps = {
  links?: HeaderLink[];
  tabs?: TabsProps['items'];
  activeTab?: string;
  onChangeTab?: (tab: string) => void;
};

export const Header = ({ tabs, activeTab, links, onChangeTab = () => undefined }: HeaderProps) => {
  return (
    <ConfigProvider
      theme={{
        components: {
          Tabs: {
            horizontalItemPadding: '14px',
            verticalItemPadding: '28px',
            itemActiveColor: '#F5F5F6',
            itemColor: '#F5F5F6',
            itemHoverColor: '#F5F5F6',
            itemSelectedColor: '#F5F5F6',
            inkBarColor: '#F5F5F6',
            titleFontSize: 14,
            horizontalMargin: '0',
          },
        },
      }}
    >
      <Styled.Container>
        <Styled.Nav>
          <Styled.Group>
            <Styled.Title>Itam</Styled.Title>
            {!!tabs?.length && <Tabs activeKey={activeTab} items={tabs} onChange={onChangeTab} centered />}
          </Styled.Group>
          <Styled.Group>
            <IconBell />
            <UserInfo />
          </Styled.Group>
        </Styled.Nav>
        {!!links?.length && <Styled.Links>
          {links.map(({ title }) => (<Link key='title' title={title} />))}
        </Styled.Links>}
      </Styled.Container>
    </ConfigProvider>
  );
};
