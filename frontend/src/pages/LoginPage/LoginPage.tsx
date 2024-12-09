import React, { useState } from 'react';
import { Header } from '../../components/Header';
import { Content } from '../../components/Content';
import * as Styled from './LoginPage.styled';
import { TextInput } from '../../components/TextInput';
import { PrimaryButton } from '../../components/PrimaryButton';

export const LoginPage = () => {
  const [isError, setError] = useState(false);
  const [login, setLogin] = useState<string>('');
  const [password, setPassword] = useState<string>('');


  const handleClick = (e: React.MouseEvent<HTMLElement, MouseEvent>) => {
    e.preventDefault();
    console.log(login);
    console.log(password)
    setError(!isError);
  };

  return (
    <Styled.Container>
      <Header links={[{ title: 'Вернуться назад' }]} />
      <Content title='Вход' links={[{ title: 'Нет аккаунта? Зарегистрироваться' }, { title: 'Забыли пароль?' }]}>
        <Styled.Form autoComplete='off'>
          {!!isError && <Styled.ErrorMessage>Введен неверный пароль. Попробуйте еще раз</Styled.ErrorMessage>}
          <TextInput id='email' placeholder='Почта/телефон' autoComplete='off' error={isError} onChange={(e)=>{setLogin(e.target.value)}}/>
          <TextInput id='password' type='password' placeholder='Пароль' autoComplete='off' error={isError} onChange={(e)=>{setPassword(e.target.value)}}/>
          <PrimaryButton type='submit' title='Войти' onClick={handleClick} />
        </Styled.Form>
      </Content>
    </Styled.Container>
  );
};
