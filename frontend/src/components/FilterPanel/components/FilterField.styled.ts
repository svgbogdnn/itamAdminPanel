import styled from "styled-components";
import ChevronIcon from '@src/assets/images/icon-chevron.svg?react';

export const Container = styled.div`
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 9px;
  padding: 0 24px;
  border-right: 0.6px solid #e0e0e033;

  &:first-child {
    padding-left: 0;
  }
`;

export const Title = styled.span`
  font-family: Nunito Sans;
  font-weight: 700;
  font-size: 14px;
  line-height: 1.36;
  padding: 14px 0;
`;

export const Icon = styled(ChevronIcon)`
  path {
    fill: #ffffff;
  }
`;
