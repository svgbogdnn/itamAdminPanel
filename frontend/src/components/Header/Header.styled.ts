import styled from "styled-components";

export const Container = styled.header`
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  width: 100%;

  .ant-tabs-nav::before {
    display: none;
  }

  .ant-tabs-tab {
    justify-content: center;
    min-width: 168px;
    font-family: Actay;
  }
`;

export const Group = styled.div`
  display: flex;
  justify-content: flex-start;
  align-items: center;
`;

export const Nav = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 4px 37px;
  background-color: #323d4e;
`;

export const Title = styled.h1`
  margin: 0;
  font-family: Nunito Sans;
  font-weight: 800;
  font-size: 30px;
  line-height: 1.364;
  text-transform: uppercase;
  color: #56FF9E;
`;

export const Links = styled.div`
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 8px;
  width: 100%;
  padding: 18px 34px;
`;
