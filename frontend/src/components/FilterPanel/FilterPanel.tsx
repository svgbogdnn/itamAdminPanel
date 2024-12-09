import React from 'react';
import * as Styled from './FilterPanel.styled';
import { ButtonWithIcon } from '../ButtonWithIcon';
import { EIcon } from '../ButtonWithIcon/ButtonWithIcon.types';
import { FilterField } from './components';
import { TFilterField } from './components/FilterField.types';

type FilterPanelProps = {
  fields: TFilterField[];
}

export const FilterPanel = ({ fields }: FilterPanelProps) => {
  return (
    <Styled.Container>
      <Styled.Group>
        {fields.map((props) => <FilterField key={props.title} {...props} />)}
      </Styled.Group>
      <Styled.Group>
        <ButtonWithIcon icon={EIcon.reset} title='Сбросить фильтр' />
      </Styled.Group>
    </Styled.Container>
  );
};
