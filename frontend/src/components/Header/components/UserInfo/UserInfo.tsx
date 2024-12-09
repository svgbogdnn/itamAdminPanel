import React from 'react';
import * as Styled from './UserInfo.styled';
import UserAvatar from '@src/assets/images/user-avatar.jpg';

export const UserInfo = () => {
  return (
    <Styled.Container>
      <Styled.Avatar src={UserAvatar} />
      <Styled.Content>
        <Styled.Name>Иван Иванов</Styled.Name>
        <Styled.Role>Admin</Styled.Role>
      </Styled.Content>
    </Styled.Container>
  );
};
