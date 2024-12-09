import React, { ButtonHTMLAttributes } from 'react';
import * as Styled from './ButtonWithIcon.styled';
import { EIcon } from './ButtonWithIcon.types';
import ResetIcon from '@src/assets/images/icon-reset.svg?react';

type ButtonWithIconProps = {
  title: string;
  icon: EIcon;
};

export const ButtonWithIcon = ({ title, icon }: ButtonHTMLAttributes<HTMLButtonElement> & ButtonWithIconProps) => {
  const renderIcon = () => {
    if (icon === EIcon.reset) {
      return <ResetIcon />;
    }

    return null;
  };

  return (
    <Styled.Button>
      <Styled.ButtonIcon>{renderIcon()}</Styled.ButtonIcon>
      <Styled.Title>{title}</Styled.Title>
    </Styled.Button>
  );
};
