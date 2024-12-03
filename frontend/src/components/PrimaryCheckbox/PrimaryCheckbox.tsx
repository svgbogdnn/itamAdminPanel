import React, { ChangeEvent, ReactElement } from 'react';
import * as Styled from './PrimaryCheckbox.styled';

type PrimaryCheckboxProps = {
  id: string;
  label?: string | ReactElement;
  name: string;
  value?: string;
  checked?: boolean;
  isSomeChecked?: boolean;
  required?: boolean;
  disabled?: boolean;
  onChange?: (e?: ChangeEvent<HTMLInputElement>) => void;
  className?: string;
  backgroundColor?: string;
};

export const PrimaryCheckbox = ({ id, label, name, value, checked, onChange, disabled, className }: PrimaryCheckboxProps) => {
  const props = {
    id,
    name,
    value,
    checked,
    onChange,
    disabled,
  };

  return (
    <Styled.Label className={className}>
      <Styled.Checkbox type='checkbox' {...props} />
      <Styled.CustomCheckbox
        $isDisabled={!!disabled}
      />
      {label && <Styled.LabelContent>{label}</Styled.LabelContent>}
    </Styled.Label>
  );
};
