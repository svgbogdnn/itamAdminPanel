import React, { useState } from 'react';
import { Container } from '../../components/Container';
import { Header } from '../../components/Header';
import { Content } from '../../components/Content';
import * as Styled from './LoginPage.styled.ts';
import { TextInput } from '../../components/TextInput';
import { PrimaryButton } from '../../components/PrimaryButton';

export const LoginPage = () => {
  const [error, setError] = useState(true);

  const handleClick = () => {
    setError(false);
  };

  return (
    <Container>
      <Header links={[{ title: 'Вернуться назад' }]} />
      <Content title='Вход' links={[{ title: 'Нет аккаунта? Зарегистрироваться' }, { title: 'Забыли пароль?' }]}>
        <Styled.Form autoComplete='off'>
          {!!error && <Styled.ErrorMessage>Введен неверный пароль. Попробуйте еще раз</Styled.ErrorMessage>}
          <TextInput id='email' placeholder='Почта/телефон' autoComplete='off' error />
          <TextInput id='password' type='password' placeholder='Пароль' autoComplete='off' error />
          <PrimaryButton type='submit' title='Войти' onClick={handleClick} />
        </Styled.Form>
      </Content>
    </Container>
  );
};
